from django import forms
from CertificationsApp.models import ModificationsType, Operation
from django.forms.widgets import FileInput

class FormLogin(forms.Form):
    id_number = forms.CharField(label="DNI", required=True)
    domain = forms.CharField(label="Patente", required=False) # Antes del chasis era required=True


class FormDoc(forms.Form):
    id_number = forms.CharField(label="DNI", required=True, widget=forms.TextInput(attrs={'readonly':'readonly'}))
    name = forms.CharField(label="Nombre", required=True)
    surname = forms.CharField(label="Apellido", required=True)
    mail = forms.EmailField(label="Email", required=True)
    phone = forms.CharField(label="Telefono", required=True, widget=forms.TextInput(
        attrs={'placeholder': "Ej: 11-6582-5214"}))
    domain = forms.CharField(label="Patente", required=False, widget=forms.TextInput(attrs={'readonly':'readonly'}))
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
    #company = forms.HiddenInput()

    image1_uploaded = forms.ImageField(label="Foto Cedula frente", help_text="Foto nitída del frente de su cedula verde", widget = FileInput)
    image2_uploaded = forms.ImageField(label="Foto Cedula reverso", help_text="Foto nitída del reverso de su cedula verde", widget = FileInput)
    image3_uploaded = forms.ImageField(label="Foto Frente", help_text="Foto de la parte posterior del vehiculo", widget = FileInput)
    image4_uploaded = forms.ImageField(label="Foto Lado derecho", help_text="Foto del vehiculo del lado del acompañante", widget = FileInput)
    image5_uploaded = forms.ImageField(label="Foto Lado izquierdo", help_text="Foto del vehiculo del lado del conductor", widget = FileInput)
    image6_uploaded = forms.ImageField(label="Foto Trasera", help_text="Foto de la parte posterior del vehiculo", widget = FileInput)
    image7_uploaded = forms.ImageField(label="Foto Detalle", required=False, help_text="Aqui insertar descripcion segun modificacion", widget = FileInput)
    image8_uploaded = forms.ImageField(label="Foto Detalle 2", required=False, help_text="Aqui insertar descripcion segun modificacion", widget = FileInput)

'''
class formCreateOperation(forms.ModelForm):

    class Meta:
        model = Operation
        fields = ()
'''

class formRegisterOperation(forms.ModelForm):

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
        )
