from django.contrib import admin
from CertificationsApp.models import Client, Company, Vehicle, ModificationsType, Operation


class ClientAdmin(admin.ModelAdmin):
    list_display = ("id_number","name", "surname", "mail", "phone")
    search_fields = ("id_number","name", "surname", "mail", "phone")

class VehicleAdmin(admin.ModelAdmin):
    list_display = ("domain","brand", "model","last_type","owner")
    search_fields = ("domain","brand", "model","last_type","owner")

class ModificationsTypeAdmin(admin.ModelAdmin):
    list_display = ("available_type","caption", "fee")
    search_fields = ("available_type","caption", "fee")

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name","cuit", "enabled")
    search_fields = ("name","cuit", "enabled")

class OperationAdmin(admin.ModelAdmin):
    list_display = ("certificate_number","stage", "owner", "id_vehicle", "original_type","final_type","registrated_at", "certificate_downloaded_at", "paid_by", "paid_at", "is_active")
    search_fields = ("certificate_number", "owner__name","id_vehicle__domain", "original_type__available_type", "paid_by", "paid_at", "is_active")
    list_filter = ("stage",)
    date_hierarchy = "registrated_at"

admin.site.register(Client, ClientAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(ModificationsType, ModificationsTypeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Operation, OperationAdmin)