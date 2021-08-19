from django.shortcuts import render, redirect
from django.http import HttpResponse
from CertificationsApp.models import Client, Vehicle, Operation


# Create your views here.
def dashboard(request):
    if request.method == "GET":

        operations = Operation.objects.select_related('id_vehicle').select_related('owner').all().order_by('-registrated_at')
        
        return render(request,"dashboard.html",{'operations':operations})

def operationDetail(request, pk):
    if request.method == "GET":
        
        operation = Operation.objects.get(pk=pk)
        vehicle = Vehicle.objects.get(pk=operation.id_vehicle.id)
        client = Client.objects.get(pk=vehicle.owner.id)


        return render(request,"operationDetail.html",{'operation':operation, 'vehicle':vehicle, 'client':client})




#player = Player.objects.select_related('terminal').select_related('terminal__node').select_related(
#    'terminal__node__channel').get(pk=player_id, operator=operator)