import pprint
from Client.forms import FormDoc
from django.forms.models import model_to_dict
from CertificationsApp.models import *
from django.core.mail import EmailMessage
from django.conf import settings
from datetime import datetime, timedelta
import os

def emailNotificationToClient(title, body, receiver):
    
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
    pprint.pprint(form)
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

def fileEraser(operation):
    '''
    1) identificar nombre archivos
     lista de nombres

    2) armar path con ese nombre  path = media/ + nombre archivo
    lista de path
    3) borrarlo
    '''
    #['image1_uploaded','image1_uploaded','image1_uploaded','image1_uploaded']
    

def filesCleaner():
    limit_date = datetime.now() - timedelta(seconds = 30)
    operations = Operation.objects.filter(certificate_downloaded_at__lte = limit_date )
    map(fileEraser, operations)