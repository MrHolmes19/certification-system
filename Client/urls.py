from django.urls import path
from . import views
#from django.conf import settings  --> por si lo necesitamos a futuro
#from django.conf.urls.static import static  --> por si lo necesitamos a futuro

# app_name = 'client-module'
urlpatterns = [
    path('', views.login, name="Login"),
    path('formulario/', views.doc, name="Doc"),
    path('formulario-pendiente/', views.waitingDoc, name="Waiting_Doc"),
]

'''path('formulario/', views.form, name="Form"),
    
    path('pago/', views.payment, name="Payment"),
    path('pago-pendiente/', views.paymentTime, name="Aprove_payment"),
    path('turno-verificacion/', views.appointment, name="Appointment"),
    path('verificacion-pendiente/', views.verificationTime, name="Aprove_verification"),
    path('certificado-pendiente/', views.certificationProcess, name="CertificationProcess"),
    path('descarga-certificado/', views.download, name="Download"),'''