from django.http.response import HttpResponseRedirect
from Client.forms import FormLogin, FormDoc, formRegisterOperation
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from CertificationsApp.models import Client, Vehicle, Operation
from .utils import loginRedirect


def login(request):
    form_login = FormLogin()
    if request.method == "POST":
        form_login = FormLogin(request.POST)
        if form_login.is_valid():
            id_number_input = request.POST.get("id_number").strip()
            domain_input = request.POST.get("domain").strip()

            targetPage = loginRedirect(id_number_input, domain_input)

            return redirect("/" + targetPage + "/")

    return render(request,"login.html",{'form_login':form_login})


def doc(request):
    login_data = request.GET
    form_doc = FormDoc(initial={'id_number':login_data.get('dni'),'domain':login_data.get('patente')})
    if request.method == "POST":
        form_doc = FormDoc(request.POST, request.FILES)
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

            operation = formRegisterOperation(request.POST, request.FILES)
            
            if operation.is_valid():

                operation = operation.save()
                id = operation.id
                zero_n = 5 - len(str(id))
                operation.certificate_number = 'CERT-{}{}'.format(zero_n*'0',str(id))
                operation.owner = client
                operation.id_vehicle = vehicle
                operation.stage = 'Documentacion enviada'
                operation.save()  
                return HttpResponseRedirect(reverse("Waiting_Doc"))
                #return redirect("client-module:Waiting_Doc")
            else:
                print(operation.errors)

        #else:
            #print("3:{}".format(form_doc.errors))
    return render(request,"doc.html",{'form_doc':form_doc})

def waitingDoc(request):   
    return render(request,"doc_checking.html")

def payment(request):   
    return render(request,"payment.html")

def waitingPayment(request):   
    return render(request,"payment_checking.html")

def appointment(request):   
    return render(request,"appointment.html")

def appointmentSuccessful(request):
    event_start_time = request.GET.get('event_start_time')
    event_date = event_start_time.split("T")[0]
    event_time = event_start_time.split("T")[1][0:5]    
    return render(request,"appointment_success.html", {'date':event_date,'time':event_time})

def waitingVerification(request):   
    return render(request,"verification_inprocess.html")

def waitingCertificate(request):   
    return render(request,"cert_inprocess.html")

def download(request):   
    return render(request,"download.html")