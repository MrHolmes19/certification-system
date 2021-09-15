from Dashboard.forms import formUpdateOperation
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from CertificationsApp.models import Client, Vehicle, Operation
from django.forms.models import model_to_dict
from pprint import pprint
from django.urls import reverse
from Client.forms import FormDoc
from .utils import emailNotificationToClient, save_doc
from Dashboard.utils import generate_form
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
        
        form, operation = generate_form(pk)

        return render(request,"operationDetail.html",{'form_doc':form, 'operation':operation})

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
                if image is not "": #esto tira warning
                    rejected_imgs[image] = "volver_a_subir.jpeg"

            operationForm = formUpdateOperation(request.POST, request.FILES, instance = operation)
            if operationForm.is_valid():
                operation.__dict__.update(**rejected_imgs)
                operation.save()  

                if request.POST.get("choice") == "approved":
                    operation.stage = 'Pendiente de pago'
                    result = emailNotificationToClient(
                        "Tu documentacion fue Aprobada",
                        "Hola {} {}, entrá al siguiente link para continuar con el trámite \n: http://localhost:8000/pago/{}".format(client.name, client.surname, operation.id),
                        client.mail
                        )
                    print("email: ", result)
                else:
                    operation.stage = 'Documentacion rechazada'
                    result = emailNotificationToClient(
                    "Tu documentacion fue Rechazada",
                    "Hola {} {}, entrá al siguiente link para continuar con el trámite \n: http://localhost:8000/formulario/{}".format(client.name, client.surname, operation.id),
                    client.mail
                    )
                    print("email: ", result)

                return HttpResponseRedirect(reverse("Dashboard:Dashboard-operations"))
            else:
                print(operationForm.errors)
        else:
            print(form_doc_update.errors)


    return render(request,"doc.html",{'form_doc':form_doc_update})


from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML


def operationDetailPDF(request, pk):

    operation = Operation.objects.get(pk=pk)
    vehicle = Vehicle.objects.get(pk=operation.id_vehicle.id)
    client = Client.objects.get(pk=vehicle.owner.id)

    html = render_to_string("pdf_template.html", {
        "operation": operation,
        "vehicle": vehicle,
        "client": client
    })
    # return render(request, "pdf_template.html", {
    #     "operation": operation,
    #     "vehicle": vehicle,
    #     "client": client
    # })

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; report.pdf"

    HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response)

    return response