from datetime import datetime, timedelta
from Certificados import settings
from CertificationsApp.models import Client, Vehicle, Operation
from django.core.mail import EmailMessage
import pytz
from django.utils import timezone

utc=pytz.UTC

# Stages of an operation (Harcoded --> Check against Client/urls.py)
stage_levels={
    "Documentacion enviada": "formulario-pendiente/",
    "Documentacion rechazada": "formulario/",
    "Pendiente de pago": "pago/",
    "Pago a revisar": "pago-en-proceso/",
    "Turno pendiente": "turno-verificacion/",
    "Verificacion pendiente": "verificacion-pendiente/",
    "Esperando certificado": "certificado-en-proceso/",
    "Certificado disponible": "descarga-certificado/",
    "Certificado expirado": "fuckyou/",
    "Operacion completada": "descarga-certificado/",
}

# Redirect from login depending on current stage of user

def loginRedirect(id_number_input, domain_input, chassis_input, company_cuit):
    client = Client.objects.filter(id_number=id_number_input).first()
    # Check if this client already exists in our database
    if client is not None:
        vehicles = client.vehicles
        for i in vehicles.all():
            coincidence = False
            # Check if this client has an operation with this domain
            if i.domain == domain_input or i.chassis_number == chassis_input:
                coincidence = True
                operations = Operation.objects.filter(id_vehicle = i.pk)
                break
        if coincidence == True:
            for x in operations:
                # Check if this vehicle has active operations
                if x.stage != "Operacion completada" or x.certificate_downloaded_at > utc.localize(datetime.now()-timedelta(days = 90)):
                    # Check if this operation is active
                    if x.is_active == False:
                        return "unable"
                    stage = x.stage
                    return stage_levels[stage] + str(x.id)
                                     
            return "formulario/?dni="+id_number_input+"&patente="+domain_input+"&chasis="+chassis_input+"&empresa="+company_cuit
        else:
            return "formulario/?dni="+id_number_input+"&patente="+domain_input+"&chasis="+chassis_input+"&empresa="+company_cuit
    else:
        return "formulario/?dni="+id_number_input+"&patente="+domain_input+"&chasis="+chassis_input+"&empresa="+company_cuit


def emailNotificationToAdmin(title, body):
    
    email = EmailMessage(subject=title, body=body, to=[settings.EMAIL_HOST_USER])
    try:
        email.send()
        return "mail succefully sended"
    except:
        return "error sending mail"


def convert_to_localtime(utctime):
    try:
        fmt = '%Y-%m-%dT%H:%M'
        utc = utctime.replace(tzinfo=pytz.UTC)
        localtz = utc.astimezone(timezone.get_current_timezone())
    except:
        return None

    return localtz.strftime(fmt)
