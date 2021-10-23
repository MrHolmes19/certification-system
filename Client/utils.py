from Certificados import settings
from CertificationsApp.models import Client, Vehicle, Operation
from django.core.mail import EmailMessage
import pytz
from django.utils import timezone

# Stages of an operation (Harcoded --> Check against Client/urls.py)
stage_levels={
    "Documentacion a revisar": "formulario-pendiente/",
    "Documentacion rechazada": "formulario/",
    "Pendiente de pago": "pago/",
    "Pago a revisar": "pago-en-proceso/",
    "Turno pendiente": "turno-verificacion/",
    "Verificacion pendiente": "verificacion-pendiente/",
    "Esperando certificado": "certificado-en-proceso/",
    "Certificado disponible": "descarga-certificado/",
    "Certificado expirado": "fuckyou/",
    "Operacion completada": "",
}

# Redirect from login depending on current stage of user

def loginRedirect(id_number_input, domain_input, company_cuit):
    client = Client.objects.filter(id_number=id_number_input).first()
    # Check if this client already exists in our database
    if client is not None:
        vehicles = client.vehicles
        for i in vehicles.all():
            coincidence = False
            # Check if this client has an operation with this domain
            if i.domain == domain_input:
                coincidence = True
                vehicle = i
                operations = i.operations
                break
        if coincidence == True:
            for x in operations.all(): ## ESTO CREO QUE ESTA MAL !!!!! PROBAR
                # Check if this vehicle has active operations
                if x.stage != "Operacion completada":
                    # Check if this operation is active
                    print(x.is_active)
                    if x.is_active == False:
                        print("----------------------efectivamente es unable")
                        return "unable"
                    stage = x.stage
                    return stage_levels[stage] + str(x.id)
                else:
                    return "formulario/?dni="+id_number_input+"&patente="+domain_input+"&empresa="+company_cuit
        else:
            return "formulario/?dni="+id_number_input+"&patente="+domain_input+"&empresa="+company_cuit
    else:
        return "formulario/?dni="+id_number_input+"&patente="+domain_input+"&empresa="+company_cuit


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