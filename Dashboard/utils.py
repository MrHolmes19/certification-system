from datetime import datetime, timedelta
import shutil

from django.http.response import HttpResponse
from Client.forms import FormDoc
from django.forms.models import model_to_dict
from CertificationsApp.models import *
from django.core.mail import EmailMessage
from django.conf import settings
from threading import Thread

def emailNotificationToClient(title, body, operation):

    receiver = operation.company.mail if operation.company else operation.owner.mail  
    email = EmailMessage(title, body, settings.EMAIL_HOST_USER, [receiver])
    try:
        email.send()
        return "mail succefully sended"
    except Exception as e:
        print(e)
        return "error sending mail"


def generate_form(pk):
    operation = Operation.objects.get(pk=pk)
    vehicle = Vehicle.objects.get(pk=operation.id_vehicle.id)
    client = Client.objects.get(pk=vehicle.owner.id)

    # converting model to dict
    operation_dict = model_to_dict(operation)
    vehicle_dict = model_to_dict(vehicle)
    client_dict = model_to_dict(client)

    # id differentiation
    operation_dict['operation_id'] = operation_dict['id']
    del operation_dict['id']
    vehicle_dict['vehicle_id'] = vehicle_dict['id']
    del vehicle_dict['id']
    client_dict['client_id'] = client_dict['id']
    del client_dict['id']

    # creating form from dict
    global_dict = operation_dict|vehicle_dict|client_dict
    form = FormDoc(initial = global_dict)
    return form, operation


def save_doc(pk, request):
    operation = Operation.objects.get(pk=pk)
    vehicle = Vehicle.objects.get(pk=operation.id_vehicle.id)
    client = Client.objects.get(pk=vehicle.owner.id)

    client_data = {
    'id_number': request.POST.get("id_number"),
    'name': request.POST.get("name"),
    'surname': request.POST.get("surname"),
    'mail': request.POST.get("mail"),
    'phone': request.POST.get("phone"),
    }
    client.__dict__.update(**client_data)
    client.save()

    vehicle_data = {
    'domain': request.POST.get("domain"),
    'brand': request.POST.get("brand"),
    'model': request.POST.get("model"),
    'last_type': request.POST.get("last_type"),
    'chassis_number': request.POST.get("chassis_number"),
    'engine_number': request.POST.get("engine_number"),
    'owner': client,
    }
    vehicle.__dict__.update(**vehicle_data)
    vehicle.save()
    return operation, client


def clean_files():

    try:
        limit_date = datetime.now() - timedelta(days = 30)
        operations = Operation.objects.filter(certificate_downloaded_at__lte = limit_date, certificate__isnull=False).exclude(certificate="")
        for operation in operations:
            operation.certificate = ""
            operation.save()
            os.chdir(settings.MEDIA_ROOT)
            shutil.rmtree(str(operation.id))
        return f"Limpieza de archivos realizada. Se borraron {len(operations)} directorios", 200
    except:
        return "Ocurrió un error durante la limpieza de archivos", 500


def schedule_reminder():

    try:
        now = datetime.now()
        limit_date = now + timedelta(days = 1)
        schedules = Operation.objects.filter(onsite_verified_at__lte = limit_date, onsite_verified_at__gte = now)
        print(len(schedules))
        for sch in schedules:
            appoinment = str(sch.onsite_verified_at.time())[0:5]
            emailNotificationToClient(
                "Recordatorio de turno",
                f"Estimado cliente lo esparamos mañana a las {appoinment} para la verificacion vehicular.\n\nVea la ruta haciendo click aqui: https://goo.gl/maps/B258sB3bcGQpa1ZJ6",
                sch)

        return f"", 200
    except:
        return "", 500