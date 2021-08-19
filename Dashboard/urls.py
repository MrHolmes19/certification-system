from django.urls import path
from . import views

app_name = 'Dashboard'

urlpatterns = [
    path('', views.dashboard, name="Dashboard"),
    path('detalle/<int:pk>', views.operationDetail, name='OperationDetail'),
]
