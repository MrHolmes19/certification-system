from Dashboard.forms import FormDocUpdate, formUpdateOperation
from django.http.response import HttpResponseRedirect
from Client.forms import FormLogin, FormDoc, formRegisterOperation
from django.shortcuts import render, redirect
from django.urls import reverse
from CertificationsApp.models import Client, ModificationsType, Vehicle, Operation
from .utils import emailNotificationToAdmin, loginRedirect
from Dashboard.utils import generate_form, save_doc
from django.core.mail import EmailMessage
import mercadopago
from pprint import pprint
from datetime import datetime

#------------------- login ------------------#
def login(request):
    form_login = FormLogin()
    if request.method == "POST":
        form_login = FormLogin(request.POST)
        if form_login.is_valid():
            id_number_input = request.POST.get("id_number").strip()
            domain_input = request.POST.get("domain").strip()

            targetPage = loginRedirect(id_number_input, domain_input)

            return redirect("/" + targetPage)

    return render(request,"login.html",{'form_login':form_login})

#------------------- Doc -> formulario ----------------#
def doc(request):
    login_data = request.GET
    form_doc = FormDoc(initial={'id_number':login_data.get('dni'),'domain':login_data.get('patente')})
    if request.method == "POST":
        form_doc = FormDoc(request.POST, request.FILES)
        if form_doc.is_valid():
            client_data = {
            'id_number': request.POST.get("id_number"),
            'name': request.POST.get("name"),
            'surname': request.POST.get("surname"),
            'mail': request.POST.get("mail"),
            'phone': request.POST.get("phone"),
            }
            client = Client.objects.create(**client_data)

            vehicle_data = {
            'domain': request.POST.get("domain"),
            'brand': request.POST.get("brand"),
            'model': request.POST.get("model"),
            'last_type': request.POST.get("last_type"),
            'chassis_number': request.POST.get("chassis_number"),
            'engine_number': request.POST.get("engine_number"),
            'owner': client,
            }
            vehicle = Vehicle.objects.create(**vehicle_data)

            operation = formRegisterOperation(request.POST, request.FILES)
            
            if operation.is_valid():

                operation = operation.save()
                id = operation.id
                zero_n = 5 - len(str(id))
                operation.certificate_number = 'CERT-{}{}'.format(zero_n*'0',str(id))
                operation.owner = client
                operation.id_vehicle = vehicle
                operation.stage = 'Documentacion enviada'
                operation.save()  

                # email sending
                email = EmailMessage("Nuevo cliente - revisar documentación",
                    "El cliente: '{} {}' acaba de cargar la documentación para certificar un '{}'".format(client_data['name'],client_data['surname'], operation.final_type),
                    "",
                    ["certificaciones.larroca@gmail.com"],
                    reply_to=[client_data['mail']])
                try:
                    email.send()
                    return HttpResponseRedirect(reverse("Waiting_Doc"))
                except:
                    print("El mail no se mandó loco")
                    return HttpResponseRedirect(reverse("Waiting_Doc"))
                #return redirect("client-module:Waiting_Doc") otra manera de hacerlo
            else:
                print(operation.errors)

        #else:
            #print("3:{}".format(form_doc.errors))
    return render(request,"doc.html",{'form_doc':form_doc})

#------------------- doc_checking -> formulario-pendiente ----------------#
def rejectedDoc(request, pk):
    if request.method == "GET":
        
        form, operation = generate_form(pk)

        return render(request,"doc.html",{'form_doc':form, 'operation':operation})

    if request.method == "POST":

        form_doc_update = FormDocUpdate(request.POST, request.FILES)
        if form_doc_update.is_valid():
            
            operation, client = save_doc(pk, request)

            operationForm = formUpdateOperation(request.POST, request.FILES, instance = operation)
            if operationForm.is_valid():
                operation.save()  

                operation.stage = 'Documentacion enviada'
                result = emailNotificationToAdmin(
                    "Documentacion Actualizada",
                    "El cliente: '{} {}' acaba de modificar la documentación para certificar un '{}'".format(client.name, client.surname, operation.final_type)
                    )
                print("client email: ", result)


                return HttpResponseRedirect(reverse("Dashboard:Dashboard-operations"))
            else:
                print(operationForm.errors)
        else:
            print(form_doc_update.errors)

#------------------- doc_checking -> formulario-pendiente ----------------#
def waitingDoc(request):   
    return render(request,"doc_checking.html")

#------------------- payment -> pago ----------------#
def payment(request, pk):
    if request.method == "GET":

        operation = Operation.objects.get(pk=pk)
        type = ModificationsType.objects.get(pk=operation.final_type.id)
        fee = type.fee

        # Adding MP credentials
        sdk = mercadopago.SDK("TEST-3332094717111517-083117-50ddb3f26d4594433d667165a99ad80b-25704844")

        # Creating the preference items
        preference_data = {
            "items": [
                {
                    "title": "Certificación por Cambio de Tipo",
                    "description": "Verificación visual del vehiculo, elaboración de informe técnico firmado por Ing. mecánico matriculado y entrega de certificado aprobado por el COPYME",
                    "quantity": 1,
                    "unit_price": fee,
                }
            ],
            # Returns after payment (Only if the form is not shown trhough a modal in the same page)
            "back_urls": {
                "success": "http://127.0.0.1:8000/turno-verificacion/" + str(pk),
                "failure": "http://127.0.0.1:8000/pago-fallido",
                "pending": "http://127.0.0.1:8000/pago-en-proceso"
            },
            "auto_return": "approved"            
        }

        preference_response = sdk.preference().create(preference_data)
        url_mp = preference_response["response"]["init_point"]
        return render(request,"payment.html",{'url':url_mp})

    return render(request,"payment.html")

#------------------- payment_checking -> pago-pendiente ----------------#
def waitingPayment(request):   
    return render(request,"payment_checking.html")

#------------------- appointment -> turno-verificacion ----------------#
def appointment(request, pk):   
    if request.method == "GET" and request.GET.get('collection_id') is not None:
        payment_data = request.GET
        payment_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        payment_type = payment_data['payment_type']
        new_stage = 'Turno pendiente'
        
        operation = Operation.objects.get(pk=pk)
        operation.paid_at = payment_date
        operation.paid_by = payment_type
        operation.stage = new_stage
        operation.save()

    return render(request,"appointment.html")

#------------------- appointment_success -> turno-verificacion-ok ----------------#
def appointmentSuccessful(request):
    if request.method == "GET":
        event_start_time = request.GET.get('event_start_time')
        event_date = event_start_time.split("T")[0]
        event_time = event_start_time.split("T")[1][0:5]  
        mail_registrated = request.GET.get('invitee_email')

        client = Client.objects.get(mail=mail_registrated)
        operation = Operation.objects.get(owner=client.id)
        operation.onsite_verified_at = event_start_time
        operation.stage = "Verificacion pendiente"
        operation.save()
    return render(request,"appointment_success.html", {'date':event_date,'time':event_time})

#------------------- verification_inprocess -> verificacion-pendiente ----------------#
def waitingVerification(request):   
    return render(request,"verification_inprocess.html")

#------------------- cert_inprocess -> certificado-en-proceso ----------------#
def waitingCertificate(request):   
    return render(request,"cert_inprocess.html")

#------------------- download -> descarga-certificado ----------------#
def download(request, pk):   
    return render(request,"download.html")
