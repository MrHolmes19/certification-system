from django.urls import path
from . import views
#from django.conf import settings  --> por si lo necesitamos a futuro
#from django.conf.urls.static import static  --> por si lo necesitamos a futuro

#app_name = 'client-module'

urlpatterns = [
    path('', views.login, name="Login"),
    path('formulario/', views.doc, name="Doc"),
    path('formulario-pendiente/', views.waitingDoc, name="Waiting_Doc"),
    path('pago/', views.payment, name="Payment"),
    path('pago-pendiente/', views.waitingPayment, name="Waiting_payment"),
    path('turno-verificacion/', views.appointment, name="Appointment"),
    path('turno-verificacion-ok/', views.appointmentSuccessful, name="appointmentSuccessful"),
    path('verificacion-pendiente/', views.waitingVerification, name="waitingVerification"),
    path('certificado-pendiente/', views.waitingCertificate, name="waitingCertificate"),
    path('descarga-certificado/', views.download, name="Download"),
]
