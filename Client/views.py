from Client.forms import FormLogin, FormDoc, formRegisterOperation
from django.shortcuts import render, redirect
from django.http import HttpResponse
from CertificationsApp.models import Client, Vehicle, Operation
from .utils import loginRedirect

# Create your views here.
def login(request):
    form_login = FormLogin()
    if request.method == "POST":
        form_login = FormLogin(request.POST)
        if form_login.is_valid():
            id_number_input = request.POST.get("id_number")
            domain_input = request.POST.get("domain")

            targetPage = loginRedirect(id_number_input, domain_input)

            return redirect("/" + targetPage + "/?id_number_client,domain_client")  # Chequear

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
        print("1:----------------------------------------------------------------------------------------------{}".format(request.FILES))
        form_doc = FormDoc(request.POST, request.FILES)
        #print("2:{}".format(form_doc))
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

            operation_data = {
            'stage': 'doc_sent',
            'original_type': request.POST.get("original_type"),
            'final_type': request.POST.get("final_type"),
            'owner': request.POST.get("mail"),
            'id_vehicle': request.POST.get("phone"),
            }
            operation = formRegisterOperation(request.POST, request.FILES)
            print('--------------')
            print('--------------')
            print('--------------')
            
            if operation.is_valid():

                operation = operation.save(commit=False)
                operation.owner = client
                operation.id_vehicle = vehicle
                operation.stage = 'doc_sent'
                operation.save()  
                print("guardado con exito")              
            else:
                print(operation.errors)

        #else:
            #print("3:{}".format(form_doc.errors))
    return render(request,"doc.html",{'form_doc':form_doc})




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