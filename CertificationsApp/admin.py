from django.contrib import admin
from CertificationsApp.models import Client, Vehicle, ModificationsType, Operation

admin.site.register(Client)
admin.site.register(Vehicle)
admin.site.register(ModificationsType)
admin.site.register(Operation)