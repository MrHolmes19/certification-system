from datetime import datetime, timedelta
from threading import Thread
from Dashboard.forms import formUpdateOperation, FormDocUpdate, formCertificate
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from CertificationsApp.models import Client, Company, ModificationsType, Vehicle, Operation, Schedule
from django.forms.models import model_to_dict
from pprint import pprint
from django.urls import reverse
from Client.forms import FormDoc
from .utils import emailNotificationToClient, save_doc, clean_files, schedule_reminder
from Client.utils import convert_to_localtime
from Dashboard.utils import generate_form
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.template.loader import render_to_string
from weasyprint import HTML
from django.conf import settings
import os, shutil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
import locale

@login_required
def dashboard(request):

    if request.method == "GET":

        operations = Operation.objects.select_related('id_vehicle').select_related('owner').all().order_by('-registrated_at')

        stage = request.GET.get('stage')
        if stage is not None and stage != 'Abiertas':
            operations = operations.filter(stage=stage)
        elif stage == 'Abiertas':
            operations = operations.exclude(stage='Operacion completada')
        
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

    appointments_list = []
    if request.method == "GET":
        
        form, operation = generate_form(pk)
        #getting appointments
        appointments = Operation.objects.all().values_list('onsite_verified_at', flat=True)
        for i in appointments:
            x = convert_to_localtime(i)
            appointments_list.append(x)

        admin_appointments = Schedule.objects.all().values_list('appointment', flat=True)
        for i in admin_appointments:
            x = convert_to_localtime(i)
            appointments_list.append(x)

        appointments_list = json.dumps(list(appointments_list), cls=DjangoJSONEncoder)       
        
        return render(request,"operationDetail.html",{'form_doc':form, 'operation':operation, "appointments_list": appointments_list})

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
                if image != "":
                    rejected_imgs[image] = "volver_a_subir.jpeg"

            operationForm = formUpdateOperation(request.POST, request.FILES, instance = operation)
            if operationForm.is_valid():
                operation.__dict__.update(**rejected_imgs)
                 
                name = operation.company.name if operation.company else f"{client.name} {client.surname}"
                if request.POST.get("choice") == "approved":

                    operation.doc_verified_at = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M')
                    jumpPay = request.POST.get("jumpPay")
                    jumpAppointment = request.POST.get("jumpAppointment")

                    if jumpPay == "true" and jumpAppointment == "true":
                        message = f"Hola {name}, Te notificaremos cuando esté disponible tu certificado"

                        operation.paid_by = "Arreglado con cliente"
                        operation.paid_amount = operation.final_type.company_fee
                        operation.stage = "Esperando certificado" 

                    elif jumpPay == "true":
                        message = f"Hola {name}, entrá al siguiente link para continuar con el trámite\
                                \n: {settings.HOST_URL}/turno-verificacion/{operation.id}"

                        operation.paid_by = "Arreglado con cliente"
                        operation.paid_amount = operation.final_type.company_fee  
                        operation.stage = "Turno pendiente"      

                    elif jumpAppointment == "true":  
                        message = f"Hola {name}, entrá al siguiente link para continuar con el trámite\
                                \n: {settings.HOST_URL}/pago/{operation.id}"

                        operation.onsite_verified_at = datetime.now()
                        operation.stage = 'Pendiente de pago'

                    else:
                        operation.stage = 'Pendiente de pago'
                        message = f"Hola {name}, entrá al siguiente link para continuar con el trámite\
                                \n: {settings.HOST_URL}/pago/{operation.id}"

                    title = "Tu documentacion fue Aprobada"
                    Thread(target = emailNotificationToClient, args = [title,message,operation]).start()
                else:
                    operation.stage = 'Documentacion rechazada'
                    
                    title = "Tu documentacion fue Rechazada"
                    body = f"Hola {name}, entrá al siguiente link para continuar con el trámite\
                            \n: {settings.HOST_URL}/formulario/{operation.id}"
                    Thread(target = emailNotificationToClient, args = [title,body,operation]).start()
                
                operation.save()
                
                return HttpResponseRedirect(reverse("Dashboard:Operations"))
            else:
                print(operationForm.errors)
        else:
            print(form_doc_update.errors)

    return render(request,"doc.html",{'form_doc':form_doc_update, "appointments_list": appointments_list})


def checkPayment(request):

    if request.method == "POST":
        pk = request.POST.get("op_id")
        approved = request.POST.get("approved")
        operation = Operation.objects.get(pk=pk)
        vehicle = Vehicle.objects.get(pk=operation.id_vehicle.id)
        client = Client.objects.get(pk=vehicle.owner.id)

        if approved == 'true':
            operation.stage = "Turno pendiente"
            operation.paid_at = datetime.now()
            operation.paid_amount = operation.final_type.fee
            
            title = f"Pago aprobado"
            body = f"Hemos recibido tu pago, por favor sacá turno para la verificacion visual: {settings.HOST_URL}/turno-verificacion/{operation.id}"
            Thread(target = emailNotificationToClient, args = [title,body,operation]).start()
            operation.save()

        if approved == 'false':

            title = request.POST.get("title")
            body = request.POST.get("body")
            amount = request.POST.get("amount")
            operation.paid_amount = amount
            operation.stage = "Pendiente de pago"
            operation.save()
            Thread(target = emailNotificationToClient, args = [title,body,operation]).start()

        return HttpResponseRedirect(reverse("Dashboard:Operations"))

def checkVerification(request):

    if request.method == "POST":
        pk = request.POST.get("op_id")
        operation = Operation.objects.get(pk=pk)
        vehicle = Vehicle.objects.get(pk=operation.id_vehicle.id)
        client = Client.objects.get(pk=vehicle.owner.id)
        action = request.POST.get("action")
    

        if action == 'cancel':
            operation.stage = "Turno pendiente"
            appointment = operation.onsite_verified_at
            operation.onsite_verified_at = None

            sch = Schedule.objects.create(appointment=appointment)

            operation.save()

            title = "Turno cancelado - volvé a reservar"
            body = f"Lo sentimos, Cancelamos tu turno por razones de fuerza mayor volve a sacarlo visitando este link: {settings.HOST_URL}/turno-verificacion/{pk}"

            Thread(target = emailNotificationToClient, args = [title,body,operation]).start()

        if action == 'reject':
            operation.stage = "Turno pendiente"
            operation.save()

            title = "Inspeccion visual rechazada - volvé a reservar"
            body = f"Rechazamos tu vehiculo, volve a sacar turno para una nueva verificacion, visitando este link: {settings.HOST_URL}/turno-verificacion/{pk}"

            Thread(target = emailNotificationToClient, args = [title,body,operation]).start()

        if action == 'aprove':
            operation.stage = "Esperando certificado"

            if not operation.onsite_verified_at:
                operation.onsite_verified_at = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M')

            operation.save()

    return HttpResponseRedirect(reverse("Dashboard:Operations"))



def appointments(request):

    if request.method == "POST":
        
        appointments = request.POST.getlist("schedule")
        day = request.POST.get("day")

        max_time = datetime.strptime(day +  " 23:59", '%Y-%m-%d %H:%M')
        min_time = datetime.strptime(day +  " 00:00", '%Y-%m-%d %H:%M')

        day_schedules = Schedule.objects.filter(appointment__lte=max_time, appointment__gte=min_time)

        for sch in day_schedules:
            sch.delete()

        for appo in appointments:
            appointment = day + " " + appo

            appointment = datetime.strptime(appointment, '%Y-%m-%d %H:%M')

            sch = Schedule.objects.create(appointment=appointment)

        return HttpResponseRedirect(reverse("Dashboard:Appointments"))
        

    appointments = Operation.objects.all().values_list('onsite_verified_at', flat=True)
    appointments_list = []
    for i in appointments:
        x = convert_to_localtime(i)
        appointments_list.append(x)

    block_list = []
    admin_appointments = Schedule.objects.all().values_list('appointment', flat=True)
    for i in admin_appointments:
        x = convert_to_localtime(i)
        block_list.append(x)
    
    appointments_list = json.dumps(list(appointments_list), cls=DjangoJSONEncoder)
    block_list = json.dumps(list(block_list), cls=DjangoJSONEncoder)
    appointments = Operation.objects.all().filter(onsite_verified_at__isnull=False, stage="Verificacion pendiente").order_by("onsite_verified_at")  #.values_list('onsite_verified_at', flat=True)
    for i in appointments:
        i.onsite_verified_at = convert_to_localtime(i.onsite_verified_at).replace("T", " ")

    return render(request,"appointments.html", {"operations": appointments, "appointments_list": appointments_list, "block_list": block_list})
    

def fees(request):

    if request.method == "GET": 
        fees = ModificationsType.objects.all()
        return render(request,"fees.html",{'fees':fees})
    
    if request.method == "POST":
        if request.POST.get("action") == "update":
            updatedFee = request.POST.get("updatedFee")
            updatedCompanyFee = request.POST.get("updatedCompanyFee")
            selected_type = request.POST.get("type")
            type = ModificationsType.objects.filter(available_type = selected_type).first()
            type.fee = updatedFee
            type.company_fee = updatedCompanyFee
            type.save()

        elif request.POST.get("action") == "updateAll":
            updatedFee = request.POST.get("updatedFee")
            updatedCompanyFee = request.POST.get("updatedCompanyFee")
            types = ModificationsType.objects.all()
            for type in types:
                type.fee = updatedFee
                type.company_fee = updatedCompanyFee
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
        # Probar esto --> operation.certificate_uploaded_at = datetime.strptime(datetime.now(), '%Y-%m-%d %H:%M')
        operation.save()
 
        title = "Certificado disponible"
        body = f"Hola {client.name} {client.surname}, Has finalizado el trámite exitosamente! \
                \n Descargá el certificado del COPIME ingresando con tus credenciales aquí: \
                \n {settings.HOST_URL}/descarga-certificado/{operation.id}"
        Thread(target = emailNotificationToClient, args = [title,body,operation]).start()

        return HttpResponseRedirect(reverse("Dashboard:Operations"))
      
    #return render(request,"doc.html",{'form_doc':form_doc_update})

def operationDetailPDF(request, pk):

    operation = Operation.objects.get(pk=pk)
    vehicle = Vehicle.objects.get(pk=operation.id_vehicle.id)
    client = Client.objects.get(pk=vehicle.owner.id)
    try:
        company = Company.objects.get(pk=operation.company.id)
    except:
        company = False

    if request.method == 'POST':
        description = request.POST.get("description")
        operation.inform_description = description
        operation.inform_created_at = datetime.now().strftime('%Y-%m-%d %H:%M')
        operation.save()
    else:
        description = operation.inform_description

    desc_list = description.split(".")

    j = 0
    for i in desc_list:
        desc_list[j] = i + "."
        j += 1
    
    
    locale.setlocale(locale.LC_TIME, "es_ES")
    date = datetime. strptime(operation.inform_created_at, '%Y-%m-%d %H:%M')
    date = datetime.strftime(date, '%d %b %Y')
    
    html = render_to_string("pdf_template.html", {
        "operation": operation,
        "description": desc_list,
        "vehicle": vehicle,
        "client": client,
        "BASE_DIR": settings.BASE_DIR,
        "STATIC_ROOT": settings.STATIC_ROOT,
        "company": company,
        "date": date,
    })

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; report.pdf"

    HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response)

    return response

def companies(request):

    if request.method == "POST" and request.POST.get("action") == "update":
        
        cuit = request.POST.get("cuit")
        name = request.POST.get("name")
        mail = request.POST.get("mail")
        phone = request.POST.get("phone")
        enabled = request.POST.get("choice")
        id = request.POST.get("id")

        company = Company.objects.get(id=id)

        company.name = name
        company.cuit = ''.join([s for s in cuit if s.isdigit()]) if cuit.isdigit() == False else cuit
        company.mail = mail
        company.phone = phone
        company.enabled = True if enabled == "enabled" else False
        company.logo = request.FILES.get("logoInput") if request.FILES.get("logoInput") else company.logo

        company.save()
    
    if request.method == "POST" and request.POST.get("action") == "new":
        
        cuit = request.POST.get("cuit")
        cuit = ''.join([s for s in cuit if s.isdigit()]) if cuit.isdigit() == False else cuit
        name = request.POST.get("name")
        mail = request.POST.get("mail")
        phone = request.POST.get("phone")
        logo = request.FILES.get("logoInput")

        company = Company.objects.create(name=name, cuit=cuit, mail=mail, phone=phone, logo=logo)
        company.save()

    try:
        companies = Company.objects.all()
    except Company.DoesNotExist:
        companies = {}

    return render(request,"company_table.html", {"companies": companies})

def inactiveOperation(request, pk):

    if request.method == "POST": 
        stateSwitch = request.POST.get("stateSwitch")       
        operation = Operation.objects.get(pk=pk)
        operation.is_active = False if not stateSwitch else True
        operation.save()
        
    return HttpResponseRedirect(reverse("Dashboard:Operations"))

def stats(request):
        
    return render(request,"stats.html")

def search(request):
    
    return render(request,"search.html")

def periodic_tasks(request):
    if request.method == 'GET':
        
        reminder_response, reminder_status = schedule_reminder()

        cleaner_response, cleaner_status = clean_files()

        return HttpResponse(200)