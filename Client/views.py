from Client.forms import FormLogin, FormDoc
from django.shortcuts import render, redirect
from django.http import HttpResponse
from CertificationsApp.models import Client, Vehicle, Operation

# Create your views here.

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

def login(request):
    form_login = FormLogin()
    if request.method == "POST":
        form_login = FormLogin(request.POST)
        if form_login.is_valid():
            id_number_input = request.POST.get("id_number")
            domain_input = request.POST.get("domain")

        client = Client.objects.filter(id_number=id_number_input)
        # Check if this client already exists in out database
        if len(client) > 0:
            vehicles = client[0].vehicles
            for i in vehicles:
                coincidence = False
                # Check if this client has this domain
                if i.domain == domain_input:
                    coincidence = True
                    vehicle = i
                    operation = i.operation
                    break                 
            if coincidence == True:
                for x in vehicles:
                    # Check if this vehicle has active operations
                    if x.stage != "ended":
                        stage = x.stage
                        return redirect("/"+stage_levels[stage]+"/?id_number_client,domain_client") #Chequear
                    else:
                        return redirect("Doc") 
            else:
                return redirect("Doc")
        else:
            return redirect("formulario/?id_number_client,domain_client")      

    return render(request,"login.html",{'form_login':form_login})
'''
si el usuario existe:  (busqueda en la tabla Client con id number y en tabla Vehicle domain --> devuelve id_operacion)
 si id_operation = stage 10:
    traeme etapa del tramite   (traer stage de la tabla Operation con ese id)
        reenvia a (pagina=etapa del tramite con un diccionario)
sino:
    Guardar datos
    Reenviar al formDoc
'''


def doc(request):
    form_doc = FormDoc()
    if request.method == "POST":
        form_doc = FormDoc(request.POST)
        if form_doc.isvalid():
            id_number = request.POST.get("id_number")
            domain = request.POST.get("domain")

    return render(request,"login.html",{'form_doc':form_doc})




"""urlpatterns = [
    path('/', views.login, name="Login"),
    path('formulario/', views.form, name="Form"),
    path('formulario-pendiente/', views.aproveTime, name="Aprove_form"),
    path('pago/', views.payment, name="Payment"),
    path('pago-pendiente/', views.paymentTime, name="Aprove_payment"),
    path('turno-verificacion/', views.appointment, name="Appointment"),
    path('verificacion-pendiente/', views.verificationTime, name="Aprove_verification"),
    path('descarga-certificado/', views.download, name="Download"),
]
"""