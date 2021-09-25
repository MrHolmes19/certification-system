from datetime import datetime
from Dashboard.forms import formUpdateOperation, FormDocUpdate, formCertificate
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from CertificationsApp.models import Client, ModificationsType, Vehicle, Operation
from django.forms.models import model_to_dict
from pprint import pprint
from django.urls import reverse
from Client.forms import FormDoc
from .utils import emailNotificationToClient, save_doc
from Client.utils import convert_to_localtime
from Dashboard.utils import generate_form
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def dashboard(request):
    if request.method == "GET":

        operations = Operation.objects.select_related('id_vehicle').select_related('owner').all().order_by('-registrated_at')

        stage = request.GET.get('stage')
        if stage is not None:
            operations = operations.filter(stage=stage)
        
        return render(request,"operation_table.html",{'operations':operations})

def dashboardClient(request):
    if request.method == "GET":

        clients = Client.objects.all()
        
        return render(request,"client_table.html",{'clients':clients})

def dashboardVehicles(request):
    if request.method == "GET":

        vehicles = Vehicle.objects.all()
        
        return render(request,"vehicle_table.html",{'vehicles':vehicles})

def operationDetail(request, pk):
    if request.method == "GET":
        
        form, operation = generate_form(pk)
        #certificateForm = formCertificate()

        return render(request,"operationDetail.html",{'form_doc':form, 'operation':operation}) #, 'form_cert':certificateForm

    if request.method == "POST":
        form_doc_update = FormDocUpdate(request.POST, request.FILES)
        if form_doc_update.is_valid():
            
            operation, client = save_doc(pk, request)

            if request.POST.get("choice") == "approved":
                operation.stage = 'Pendiente de pago'
            else:
                operation.stage = 'Documentacion rechazada'

            rejected_images = request.POST.get("rejectedImages")
            rejected_images = rejected_images.split("-")
            rejected_imgs = {}
            for image in set(rejected_images):
                if image != "": #Se cambio el "is not" ya que tiraba warning
                    rejected_imgs[image] = "volver_a_subir.jpeg"

            operationForm = formUpdateOperation(request.POST, request.FILES, instance = operation)
            if operationForm.is_valid():
                operation.__dict__.update(**rejected_imgs)
                operation.save()  

                if request.POST.get("choice") == "approved":
                    operation.stage = 'Pendiente de pago'
                    result = emailNotificationToClient(
                        "Tu documentacion fue Aprobada",
                        "Hola {} {}, entrá al siguiente link para continuar con el trámite\
                            \n: http://localhost:8000/pago/{}".format(client.name, client.surname, operation.id),
                        client.mail
                        )
                    print("email: ", result)
                else:
                    operation.stage = 'Documentacion rechazada'
                    result = emailNotificationToClient(
                    "Tu documentacion fue Rechazada",
                    "Hola {} {}, entrá al siguiente link para continuar con el trámite\
                        \n: http://localhost:8000/formulario/{}".format(client.name, client.surname, operation.id),
                    client.mail
                    )
                    print("email: ", result)

                return HttpResponseRedirect(reverse("Dashboard:Dashboard-operations"))
            else:
                print(operationForm.errors)
        else:
            print(form_doc_update.errors)

    return render(request,"doc.html",{'form_doc':form_doc_update})

'''
def acceptPayment(request, pk, estado):

    if request.method == "POST":
        operation = Operation.objects.get(pk=pk)
        operation.stage = "Turno pendiente"
        operation.paid_at = datetime.now()

        operation.save()
        print("Entre a accept Payment")
        return HttpResponseRedirect(reverse("Dashboard:Dashboard-operations"))
    
    
def rejectPayment(request, pk, estado):

    if request.method == "POST":
        operation = Operation.objects.get(pk=pk)
        operation.stage = "Pago pendiente"
        operation.save()
        print("Entre a reject Payment")
        return HttpResponseRedirect(reverse("Dashboard:Dashboard-operations"))  
'''

def checkPayment(request):

    if request.method == "POST":
        pk = request.POST.get("op_id")
        approved = request.POST.get("approved")
        operation = Operation.objects.get(pk=pk)

        if approved == 'true':
            operation.stage = "Turno pendiente"
            operation.paid_at = datetime.now()
            operation.paid_amount = operation.final_type.fee
            print(operation.final_type.fee)
            operation.save()

            return HttpResponseRedirect(reverse("Dashboard:Dashboard-operations")) #No conviene dejar uno solo?

        if approved == 'false':
            operation = Operation.objects.get(pk=pk)
            vehicle = Vehicle.objects.get(pk=operation.id_vehicle.id)
            client = Client.objects.get(pk=vehicle.owner.id)

            title = request.POST.get("title")
            body = request.POST.get("body")
            amount = request.POST.get("amount")
            operation.paid_amount = amount
            operation.save()
            result = emailNotificationToClient(title,body,client.mail)

            return HttpResponseRedirect(reverse("Dashboard:Dashboard-operations"))


def appoinments(request):

    appointments = Operation.objects.all().values_list('onsite_verified_at', flat=True)
    appointments_list = []
    for i in appointments:
        x = convert_to_localtime(i)
        appointments_list.append(x)
    appointments_list = json.dumps(list(appointments_list), cls=DjangoJSONEncoder)
    appointments = Operation.objects.all().filter(onsite_verified_at__isnull=False, stage="Verificacion pendiente").order_by("onsite_verified_at")  #.values_list('onsite_verified_at', flat=True)

    for i in appointments:
        i.onsite_verified_at = convert_to_localtime(i.onsite_verified_at).replace("T", " ")

    #appointments_list = json.dumps(list(appointments_list), cls=DjangoJSONEncoder) 
    print(appointments)
    return render(request,"appointments.html", {"operations": appointments, "appointments_list": appointments_list})


def fees(request):

    if request.method == "GET": 
        fees = ModificationsType.objects.all()
        return render(request,"fees.html",{'fees':fees})
    
    if request.method == "POST":
        if request.POST.get("action") == "update":
            updatedFee = request.POST.get("updatedFee")
            selected_type = request.POST.get("type")
            type = ModificationsType.objects.filter(available_type = selected_type).first()
            type.fee = updatedFee
            type.save()

        elif request.POST.get("action") == "updateAll":
            updatedFee = request.POST.get("updatedFee")
            types = ModificationsType.objects.all()
            for type in types:
                type.fee = updatedFee
                type.save()
    return HttpResponseRedirect(reverse("Dashboard:Fees"))


def certificate(request):
    
    if request.method == "POST":
        pk = request.POST.get("op_id")
        operation = Operation.objects.get(pk=pk)
        client = Client.objects.filter(id = operation.owner_id).first()

        file = request.FILES['certificateInput']
        operation.certificate = file
        operation.stage = "Certificado disponible"
        operation.certificate_uploaded_at = datetime.now()
        operation.save()
 
        result = emailNotificationToClient(
            "Certificado disponible",
            "Hola {} {}, Has finalizado el trámite exitosamente! \
                \n Descargá el certificado del COPIME ingresando con tus credenciales aquí: \
                \n http://localhost:8000/descarga-certificado/{}".format(client.name, client.surname, operation.id),
            client.mail
            )
        print("email: ", result)

        return HttpResponseRedirect(reverse("Dashboard:Dashboard-operations"))
      
    #return render(request,"doc.html",{'form_doc':form_doc_update})