from django.db import models

class ModificationsType(models.Model):
    available_type = models.CharField(max_length=64)
    caption = models.CharField(max_length=256)
    fee = models.IntegerField()

    class Meta:
        verbose_name = 'type'
        verbose_name_plural = 'types'
    
    def __str__(self):
        return self.available_type
    
class Client(models.Model):    
    id_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    mail = models.EmailField(max_length=64, unique=True)
    #phone = models.PhoneNumberField(null=False, blank=False, unique=True)
    phone = models.IntegerField(blank=False, unique=True)

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
    
    def __str__(self):
        return "{} {}".format(self.name, self.surname) #OJO acá lo cambié porque me saltaba error en el admin al cargar

class Vehicle(models.Model):    
    domain = models.CharField(max_length=7)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=64)
    last_type = models.ForeignKey(ModificationsType, related_name='finaltype', on_delete=models.SET_NULL, null=True)
    chassis_number = models.CharField(max_length=64)
    engine_number = models.CharField(max_length=64)
    owner = models.ForeignKey(Client, related_name='vehicles', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'vehicle'
        verbose_name_plural = 'vehicles'
    
    def __str__(self):
        return str(self.domain)


class Operation(models.Model):    
    certificate_number = models.CharField(max_length=64)
    stage = models.CharField(max_length=64)
    registrated_at = models.DateTimeField(auto_now_add=True)
    image1_uploaded = models.ImageField(upload_to="images")
    image2_uploaded = models.ImageField(upload_to="images")
    image3_uploaded = models.ImageField(upload_to="images")
    image4_uploaded = models.ImageField(upload_to="images")
    image5_uploaded = models.ImageField(upload_to="images")
    image6_uploaded = models.ImageField(upload_to="images", blank=True, null=True)
    image7_uploaded = models.ImageField(upload_to="images", blank=True, null=True)
    paid_at = models.DateTimeField(default=None, blank=True, null=True) #Puede llegar a joder el None
    paid_by = models.CharField(max_length=64, blank=True, null=True)
    doc_verified_at = models.DateTimeField(default=None, blank=True, null=True)
    onsite_verified_at = models.DateTimeField(default=None, blank=True, null=True)
    inform_created_at = models.DateTimeField(default=None, blank=True, null=True)
    certificate_uploaded_at = models.DateTimeField(default=None, blank=True, null=True)
    certificate_downloaded_at = models.DateTimeField(default=None, blank=True, null=True)
    owner = models.ForeignKey(Client, related_name='operations', on_delete=models.SET_NULL, null=True)
    id_vehicle = models.ForeignKey(Vehicle, related_name='operations', on_delete=models.SET_NULL, null=True)
    original_type = models.ForeignKey(ModificationsType, related_name='original', on_delete=models.SET_NULL, null=True)
    final_type = models.ForeignKey(ModificationsType, related_name='final', on_delete=models.SET_NULL, null=True)
    #is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'operation'
        verbose_name_plural = 'operations'
    
    def __str__(self):
        return self.certificate_number
