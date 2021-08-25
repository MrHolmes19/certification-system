from django.urls import path
from . import views

app_name = 'Dashboard'

urlpatterns = [
    path('', views.dashboard, name="Dashboard-operations"),
    path('Clientes', views.dashboardClient, name="Dashboard-clients"),
    path('Vehiculos', views.dashboardVehicles, name="Dashboard-vehicles"),
    path('detalle/<int:pk>', views.operationDetail, name='OperationDetail'),
    path('borrador', views.borrador, name='borrador'),
]
