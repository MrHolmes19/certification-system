from CertificationsApp.models import Client, Vehicle, Operation

stage_levels={
    "doc_sent": "formulario-pendiente",
    "doc_rejected": "formulario",
    "doc_aproved": "pago",
    "payment_done": "pago-pendiente",
    "payment_aproved": "turno-verificacion",
    "appointment_confirmed": "verificacion-pendiente",
    "verification_aproved": "certificado-pendiente",
    "certificate_available": "download",
    "certificate_expired": "fuckyou",
    "operation_ended": "",
}

def loginRedirect(id_number_input, domain_input):
    client = Client.objects.filter(id_number=id_number_input).first()
    # Check if this client already exists in out database
    if client is not None:
        vehicles = client.vehicles
        for i in vehicles.all():
            coincidence = False
            # Check if this client has this domain
            if i.domain == domain_input:
                coincidence = True
                vehicle = i
                operations = i.operations
                break
        if coincidence == True:
            for x in operations.all():
                # Check if this vehicle has active operations
                if x.stage != "ended":
                    stage = x.stage
                    return stage_levels[stage] # Chequear
                else:
                    return "formulario"
        else:
            return "formulario"
    else:
        return "formulario"