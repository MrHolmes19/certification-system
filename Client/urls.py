from django.urls import path
from . import views
#from django.conf import settings  --> por si lo necesitamos a futuro
#from django.conf.urls.static import static  --> por si lo necesitamos a futuro

#app_name = 'client-module'

urlpatterns = [
    path('', views.login, name="Login"),
    path('formulario/', views.doc, name="Doc"),
    path('formulario-pendiente/', views.waitingDoc, name="Waiting_Doc"),
    path('pago/<int:pk>', views.payment, name="Payment"),
    path('pago-en-proceso/', views.waitingPayment, name="Waiting_payment"),
    path('turno-verificacion/<int:pk>', views.appointment, name="Appointment"),
    path('turno-verificacion-ok/', views.appointmentSuccessful, name="AppointmentSuccessful"),
    path('verificacion-pendiente/', views.waitingVerification, name="WaitingVerification"),
    path('certificado-en-proceso/', views.waitingCertificate, name="WaitingCertificate"),
    path('descarga-certificado/<int:pk>', views.download, name="Download"),
]
