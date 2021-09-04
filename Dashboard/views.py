from Dashboard.forms import formUpdateOperation
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from CertificationsApp.models import Client, Vehicle, Operation
from django.forms.models import model_to_dict
from pprint import pprint
from django.urls import reverse
from Client.forms import FormDoc
from .utils import emailNotification
from Dashboard.forms import FormDocUpdate

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

        return render(request,"operationDetail.html",{'form_doc':form, 'operation':operation})

    if request.method == "POST":
        form_doc_update = FormDocUpdate(request.POST, request.FILES)
        if form_doc_update.is_valid():
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
            #vehicle.objects.update(**vehicle_data)  

            if request.POST.get("choice") == "approved":
                operation.stage = 'Pendiente de pago'
            else:
                operation.stage = 'Documentacion rechazada'

            
            rejected_images = request.POST.get("rejectedImages")
            rejected_images = rejected_images.split("-")

            rejected_imgs = {}
            for image in set(rejected_images):
                if image is not "":
                    rejected_imgs[image] = "volver_a_subir.jpeg"

            operationForm = formUpdateOperation(request.POST, request.FILES, instance = operation)
            if operationForm.is_valid():
                operation.__dict__.update(**rejected_imgs)
                operation.save()  

                if request.POST.get("choice") == "approved":
                    result = emailNotification(
                        "Tu documentacion fue Aprobada",
                        "Hola {} {}, entrá al siguiente link para continuar con el trámite /n: http://localhost:8000/pago/{}".format(client.name, client.surname, operation.id),
                        client.mail
                        )
                else:
                    operation.stage = 'Documentacion rechazada'

                return HttpResponseRedirect(reverse("Dashboard:Dashboard-operations"))
            else:
                print(operationForm.errors)
        else:
            print(form_doc_update.errors)


    return render(request,"doc.html",{'form_doc':form_doc_update})


#player = Player.objects.select_related('terminal').select_related('terminal__node').select_related(
#    'terminal__node__channel').get(pk=player_id, operator=operator)