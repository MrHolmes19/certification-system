from django.urls import path
from . import views

app_name = 'Dashboard'

urlpatterns = [
    path('', views.dashboard, name="Dashboard-operations"),
    path('Clientes', views.dashboardClient, name="Dashboard-clients"),
    path('Vehiculos', views.dashboardVehicles, name="Dashboard-vehicles"),
    path('detalle/<int:pk>', views.operationDetail, name='OperationDetail'),
    #path('detalle/<int:pk>/<str:estado>', views.acceptPayment, name='Accept-payment'),
    #path('detalle/<int:pk>/<str:estado>', views.rejectPayment, name='Reject-payment'),
    path('detalle/validar-pago', views.checkPayment, name='Check-payment'),
    #path('detalle/validar-verificacion', views.checkVerification, name='Check-verification'),
    path('detalle/certificado', views.certificate, name='Certificate'),
    path('detalle/<int:pk>/pdf', views.operationDetailPDF, name='OperationCertificate'),
    path('turnos', views.appointments, name='Appointments'),
    path('tarifas', views.fees, name='Fees'),
]
