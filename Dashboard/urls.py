from django.urls import path
from . import views

app_name = 'Dashboard'

urlpatterns = [
    path('', views.dashboard, name="Dashboard-operations"),
    path('Clientes', views.dashboardClient, name="Dashboard-clients"),
    path('Vehiculos', views.dashboardVehicles, name="Dashboard-vehicles"),
    path('detalle/<int:pk>', views.operationDetail, name='OperationDetail'),
    path('detalle/<int:pk>/<str:estado>', views.acceptPayment, name='Accept-payment'), #Cambiar
    path('detalle/<int:pk>/<str:estado>', views.rejectPayment, name='Reject-payment'), #Cambiar
    path('detalle/validar-pago', views.checkPayment, name='Check-payment'),
    path('turnos', views.appoinments, name='Appoinments'),
]
