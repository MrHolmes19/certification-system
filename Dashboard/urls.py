from django.urls import path, include
from . import views

app_name = 'Dashboard'

urlpatterns = [
    path('auth/', include("django.contrib.auth.urls")),

    path('', views.dashboard, name="Operations"),
    path('Clientes', views.dashboardClient, name="Clients"),
    path('Empresas', views.companies, name='Companies'),
    path('Vehiculos', views.dashboardVehicles, name="Vehicles"),
    path('detalle/<int:pk>', views.operationDetail, name='OperationDetail'),
    path('detalle/validar-pago', views.checkPayment, name='Check-payment'),
    path('detalle/validar-verificacion', views.checkVerification, name='Check-verification'),
    path('detalle/certificado', views.certificate, name='Certificate'),
    path('detalle/<int:pk>/pdf', views.operationDetailPDF, name='Operation-pdf'),
    path('detalle/<int:pk>/inactive', views.inactiveOperation, name='InactiveOperation'),
    path('turnos', views.appointments, name='Appointments'),
    path('tarifas', views.fees, name='Fees'),
    path('Estadisticas', views.stats, name='Stats'),
    path('Busqueda', views.search, name='Search'),
    
]
