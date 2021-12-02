from threading import Thread
from Certificados.settings import BASE_DIR
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import HttpResponseRedirect
from Client.forms import FormLogin, FormDoc, formRegisterOperation, formUpdateOperation
from django.shortcuts import render, redirect
from django.urls import reverse
from CertificationsApp.models import Client, Company, ModificationsType, Schedule, Vehicle, Operation
from .utils import emailNotificationToAdmin, loginRedirect
from Dashboard.utils import emailNotificationToClient, generate_form, save_doc
from django.core.mail import EmailMessage
import mercadopago
from pprint import pprint
import json
from datetime import datetime
from .utils import convert_to_localtime
import os, shutil
from django.conf import settings
from django.http import HttpResponse, Http404
import mimetypes
from django.template.loader import render_to_string
from weasyprint import HTML


#------------------- login ------------------#
def login(request):
    form_login = FormLogin()
    if request.method == "POST":

        # If company
        company_cuit = request.POST.get("cuit")
        if company_cuit != "":   
            try:
                company = Company.objects.get(cuit=company_cuit)
            except Company.DoesNotExist:
                return render(request,"login.html",{'form_login':form_login, "message": "Este CUIT no es valido, contactese con el administrador de la pagina"})

        form_login = FormLogin(request.POST)
        if form_login.is_valid():
            id_number_input = request.POST.get("id_number").strip()
            domain_input = request.POST.get("domain").strip()

            # input transformation
            if id_number_input.isdigit() == False:
                numbers = [s for s in id_number_input if s.isdigit()]
                id_number_input = ''.join(numbers)

            if domain_input.isalnum() == False:
                alphanumerics = [s for s in domain_input if s.isalnum()]
                domain_input = ''.join(alphanumerics)

            # redirection manager
            targetPage = loginRedirect(id_number_input, domain_input, company_cuit)
            if targetPage == "unable":
                return render(request,"login.html",{'form_login':form_login, "message": "No es posible continuar con el trámite. Contáctenos a la brevedad vía mail o teléfono"})
            return redirect("/" + targetPage)

    return render(request,"login.html",{'form_login':form_login})

#------------------- Doc -> formulario ----------------#
def doc(request):
    login_data = request.GET
    form_doc = FormDoc(initial={'id_number':login_data.get('dni'),'domain':login_data.get('patente')})

    if request.method == "POST":

        # input transformation
        phone = request.POST.get("phone").strip()
        if phone.isdigit() == False:
            numbers = [s for s in phone if s.isdigit()]
            phone = ''.join(numbers)

        form_doc = FormDoc(request.POST, request.FILES)

        if form_doc.is_valid():
            client_data = {
            'id_number': request.POST.get("id_number"),
            'name': request.POST.get("name"),
            'surname': request.POST.get("surname"),
            'mail': request.POST.get("mail"),
            'phone': phone,
            #'phone': request.POST.get("phone"),
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

            operation = Operation.objects.create() # Necesary to generate instance and create path before saving images
            operation = formRegisterOperation(request.POST, request.FILES, instance = operation)

            if operation.is_valid():

                operation = operation.save()
                id = operation.id
                zero_n = 5 - len(str(id))
                operation.certificate_number = 'CERT-{}{}'.format(zero_n*'0',str(id))
                operation.owner = client
                operation.id_vehicle = vehicle
                operation.stage = 'Documentacion enviada'

                if request.POST.get("company") != "":
                    company = Company.objects.get(cuit=request.POST.get("company"))
                    operation.company = company
                
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
                    print("El mail no se mandó")
                    return HttpResponseRedirect(reverse("Waiting_Doc"))
                #return redirect("client-module:Waiting_Doc") otra manera de hacerlo
            else:
                print(operation.errors)
        else:
            print("3:{}".format(form_doc.errors))
    #company=login_data.get('empresa')
    if login_data.get('empresa')!="":
        print(request.GET.get('empresa'))
        company = Company.objects.get(cuit=login_data.get('empresa'))
    else:
        company = ""
    return render(request,"doc.html",{'form_doc':form_doc, "company":company})

#------------------- doc_checking -> formulario-pendiente ----------------#
def rejectedDoc(request, pk):
    if request.method == "GET":
        
        form, operation = generate_form(pk)

        return render(request,"doc.html",{'form_doc':form, 'operation':operation})

    if request.method == "POST":
        
        operation = Operation.objects.get(pk=pk)
        vehicle = Vehicle.objects.get(pk=operation.id_vehicle.id)
        client = Client.objects.get(pk=vehicle.owner.id)        

        operationForm = formUpdateOperation(request.POST, request.FILES, instance = operation)
        if operationForm.is_valid():
            operation.save()  

            operation.stage = 'Documentacion enviada'

            title = "Documentacion Actualizada"
            body = f"El cliente: '{client.name} {client.surname}' acaba de modificar la documentación para certificar un '{operation.final_type}'"
            Thread(target = emailNotificationToAdmin, args = [title,body]).start()

            return HttpResponseRedirect(reverse("Waiting_Doc"))
        else:
            print(operationForm.errors)
            return HttpResponseRedirect(reverse("Waiting_Doc"))


#------------------- doc_checking -> formulario-pendiente ----------------#
def waitingDoc(request):   
    return render(request,"doc_checking.html", {"admin_email": settings.EMAIL_HOST_USER})

#------------------- payment -> pago ----------------#
def payment(request, pk):
    if request.method == "GET":

        operation = Operation.objects.get(pk=pk)
        type = ModificationsType.objects.get(pk=operation.final_type.id)

        if operation.company:
            fee = type.company_fee - operation.paid_amount
        else:
            fee = type.fee - operation.paid_amount

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
                "success": "settings.HOST_URL/turno-verificacion/" + str(pk),
                "failure": "settings.HOST_URL/pago-fallido",
                "pending": "settings.HOST_URL/pago-en-proceso"
            },
            "auto_return": "approved",
            "payment_methods": {
                "excluded_payment_types": [
                {
                    #"id": "atm"
                },
                {
                    #"id": "ticket"
                }
            ],            
        }
    }
        preference_response = sdk.preference().create(preference_data)
        url_mp = preference_response["response"]["init_point"]
        return render(request,"payment.html",{'url':url_mp, "fee": fee, "operation_id": operation.pk})

    return render(request,"payment.html")

#------------------- payment_fail -> pago-fallido ----------------#
def paymentFail(request):   
    return render(request,"payment_failed.html")


#------------------- payment_checking -> pago-pendiente ----------------#
def waitingPayment(request, pk):

    operation = Operation.objects.get(pk=pk)
    vehicle = Vehicle.objects.get(pk=operation.id_vehicle.id)
    client = Client.objects.get(pk=vehicle.owner.id)

    operation.paid_by = "Transferencia Bancaria"
    operation.stage = "Pago a revisar"
    operation.save()

    title = "Pago Efectuado"
    body = f"El cliente: '{client.name} {client.surname}' notifica que realizo una tranferencia correspondiente al informe {operation.certificate_number}"
    Thread(target = emailNotificationToAdmin, args = [title,body]).start()

    return render(request,"payment_checking.html", {"operation": operation, "admin_email": settings.EMAIL_HOST_USER})

#------------------- appointment -> turno-verificacion ----------------#
def appointment(request, pk):   
    if request.method == "GET" and request.GET.get('collection_id') is not None:
        payment_data = request.GET
        payment_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        payment_type = payment_data['payment_type']
        new_stage = 'Turno pendiente'

        operation = Operation.objects.get(pk=pk)

        # checkeo si tiene fecha de verificacion como flag para saber si se salta la seleccion de turno
        if operation.onsite_verified_at:
            operation.onsite_verified_at = None
            operation.stage = "Esperando certificado"
            operation.save()
            return render(request,"download_inprocess_.html", {"admin_email": settings.EMAIL_HOST_USER})

        amount = operation.final_type.fee
        print(amount)
        operation.paid_amount = amount
        operation.paid_at = payment_date
        operation.paid_by = payment_type
        operation.stage = new_stage
        operation.save()

    if request.method == "POST":
        
        operation = Operation.objects.get(pk=pk)
        day = request.POST.get("day")
        schedule = request.POST.get("schedule")

        appointment = day + " " + schedule
        #print(appointment)
        operation.onsite_verified_at = datetime.strptime(appointment, '%Y-%m-%d %H:%M')
        operation.stage = "Verificacion pendiente"
        operation.save()
        domain = operation.id_vehicle.domain

        if request.POST.get("admin"):

            message = f"Tu turno para la inspeccion visual fue reservado para el {day} a las {schedule}"
            
            result = emailNotificationToClient(
                f"Turno para la verificacion de {domain}",
                message,
                operation
                )

            return HttpResponseRedirect(reverse("Dashboard:Operations"))

            

        return render(request,"verification_inprocess.html", {"date":day, "time":schedule})

    operation = Operation.objects.get(pk=pk)
    appointments = Operation.objects.all().values_list('onsite_verified_at', flat=True)
    appointments_list = []
    for i in appointments:
        x = convert_to_localtime(i)
        appointments_list.append(x)

    admin_appointments = Schedule.objects.all().values_list('appointment', flat=True)
    for i in admin_appointments:
        x = convert_to_localtime(i)
        appointments_list.append(x)

    appointments_list = json.dumps(list(appointments_list), cls=DjangoJSONEncoder) 
    #print(appointments_list)
    return render(request,"appointment.html", {"operation":operation, "appointments_list": appointments_list})

''' NO VA MAS. ERA PARA EL CALENDLY
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
'''

#------------------- verification_inprocess -> verificacion-pendiente ----------------#
def waitingVerification(request, pk):   
    operation = Operation.objects.get(pk=pk)
    schedule = operation.onsite_verified_at
    date = datetime.strftime(schedule, '%d-%m-%Y')
    time = datetime.strftime(schedule, '%H:%M')
    return render(request,"verification_inprocess.html", {'date':date,'time':time})

#------------------- cert_inprocess -> certificado-en-proceso ----------------#
def waitingCertificate(request, pk):
    operation = Operation.objects.get(pk=pk)

    return render(request,"download_inprocess_.html", {"admin_email": settings.EMAIL_HOST_USER})

#------------------- download -> descarga-certificado ----------------#

def download(request, pk, path):   
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

    return render(request,"download.html")

def download(request, pk):  

    operation = Operation.objects.get(pk=pk)

    return render(request,"download.html", {"operation" : operation})


def download_certificate(request, pk):  

    operation = Operation.objects.get(pk=pk)
    vehicle = Vehicle.objects.get(pk=operation.id_vehicle.id)
    certFile = operation.certificate

    filepath = str(settings.MEDIA_ROOT) + "/" + str(certFile)

    filename = "{} - {}.pdf".format(operation.certificate_number, vehicle.domain)
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename

    if operation.certificate_downloaded_at:
        operation.stage = "Operacion completada"

    operation.certificate_downloaded_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #eliminar esta linea
    operation.save()  

    return response

def download_inform(request, pk):  

    operation = Operation.objects.get(pk=pk)
    vehicle = Vehicle.objects.get(pk=operation.id_vehicle.id)
    client = Client.objects.get(pk=vehicle.owner.id)

    description = operation.inform_description
    desc_list = description.split(".")

    j = 0
    for i in desc_list:
        desc_list[j] = i + "."
        j += 1

    #print(desc_list)
    html = render_to_string("pdf_template.html", {
        "operation": operation,
        "description": desc_list,
        "vehicle": vehicle,
        "client": client
    })

    filename = "Informe-{}".format(vehicle.domain)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=%s" % filename

    HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response)

    if operation.certificate_downloaded_at:
        operation.stage = "Operacion completada"

    operation.certificate_downloaded_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    operation.save()  

    return response