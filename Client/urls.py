from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="Login"),
    path('formulario/', views.doc, name="Doc"),
    path('formulario/<int:pk>', views.rejectedDoc, name="Rejected_Doc"),
    path('formulario-pendiente/<int:pk>', views.waitingDoc, name="Waiting_Doc"),
    path('pago/<int:pk>', views.payment, name="Payment"),
    path('pago-en-proceso/<int:pk>', views.waitingPayment, name="Waiting_payment"),
    path('pago-fallido/', views.paymentFail, name="Payment_fail"),
    path('turno-verificacion/<int:pk>', views.appointment, name="Appointment"),
    path('verificacion-pendiente/<int:pk>', views.waitingVerification, name="WaitingVerification"),
    path('certificado-en-proceso/<int:pk>', views.waitingCertificate, name="WaitingCertificate"),
    path('descarga-certificado/<int:pk>', views.download, name="Download"),
    path('certificate-file/<int:pk>', views.download_certificate, name="DownloadCertificate"),
    path('inform-file/<int:pk>', views.download_inform, name="DownloadInform"),
]
