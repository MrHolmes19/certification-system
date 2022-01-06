from django import forms
from CertificationsApp.models import Operation, ModificationsType

class formUpdateOperation(forms.ModelForm):

    image1_uploaded = forms.ImageField(required=False)
    image2_uploaded = forms.ImageField(required=False)
    image3_uploaded = forms.ImageField(required=False)
    image4_uploaded = forms.ImageField(required=False)
    image5_uploaded = forms.ImageField(required=False)   
    image6_uploaded = forms.ImageField(required=False)
    image7_uploaded = forms.ImageField(required=False)
    image8_uploaded = forms.ImageField(required=False)

    class Meta:
        model = Operation
        fields = (
            'image1_uploaded',
            'image2_uploaded',
            'image3_uploaded',
            'image4_uploaded',
            'image5_uploaded',
            'image6_uploaded',
            'image7_uploaded',
            'image8_uploaded',
            'original_type',
            'final_type',
        )

class FormDocUpdate(forms.Form):
    id_number = forms.CharField(label="DNI", required=True)
    name = forms.CharField(label="Nombre", required=True)
    surname = forms.CharField(label="Apellido", required=True)
    mail = forms.EmailField(label="Email", required=True)
    phone = forms.CharField(label="Telefono", required=True, widget=forms.TextInput(
        attrs={'placeholder': "Ej: 11-6582-5214"}))
    domain = forms.CharField(label="Patente", required=False)
    brand = forms.CharField(label="Marca", required=True, widget=forms.TextInput(
        attrs={'placeholder': "Ej: Ford"}))
    model = forms.CharField(label="Modelo", required=True, widget=forms.TextInput(
        attrs={'placeholder': "Ej: Transit"}))
    chassis_number = forms.CharField(label="Nº de chasis", required=True)
    engine_number = forms.CharField(label="Nº de motor", required=True)
    original_type = forms.ModelChoiceField(queryset=ModificationsType.objects.all(), 
        label="Vehiculo actual", required=True)
    final_type = forms.ModelChoiceField(queryset=ModificationsType.objects.all(),
        label="Vehiculo a homologar", required=True)


class formCertificate(forms.ModelForm):
    certificate = forms.FileField(required=False)