from django import forms
from CertificationsApp.models import ModificationsType, Operation

typelist = [
    ("tipo1", "tipo1"), ("tipo2", "tipo2"), ("tipo3", "tipo3")
]


class FormLogin(forms.Form):
    id_number = forms.CharField(label="DNI", required=True)
    domain = forms.CharField(label="Patente", required=True)


class FormDoc(forms.Form):
    id_number = forms.CharField(label="DNI", required=True)
    name = forms.CharField(label="Nombre", required=True)
    surname = forms.CharField(label="Apellido", required=True)
    mail = forms.EmailField(label="Email", required=True)
    phone = forms.CharField(label="Telefono", required=True)

    domain = forms.CharField(label="Patente", required=True)
    brand = forms.CharField(label="Marca", required=True)
    model = forms.CharField(label="Modelo", required=True)
    chassis_number = forms.CharField(label="Nº de chasis", required=True)
    engine_number = forms.CharField(label="Nº de motor", required=True)
    original_type = forms.ModelChoiceField(queryset=ModificationsType.objects.all(), label="Tipo actual",
                                           required=True)
    # original_type2 = forms.CharField(label="Tipo actual (charfield)",
    #                                  required=True, widget=forms.Select(choices=typelist))
    final_type = forms.ModelChoiceField(queryset=ModificationsType.objects.all(), label="Tipo final",
                                           required=True)

    image1_uploaded = forms.ImageField(label="Foto Cedula")
    image2_uploaded = forms.ImageField(label="Foto Frente")
    image3_uploaded = forms.ImageField(label="Foto lateral 1")
    image4_uploaded = forms.ImageField(label="Foto lateral 2")
    image5_uploaded = forms.ImageField(label="Foto trasera")
    image6_uploaded = forms.ImageField(label="Foto detalle", required=False)
    image7_uploaded = forms.ImageField(label="Foto detalle 2", required=False)

class formRegisterOperation(forms.ModelForm):
    class Meta:
        model = Operation
        fields = (
            #'stage', 
            'image1_uploaded',
            'image2_uploaded',
            'image3_uploaded',
            'image4_uploaded',
            'image5_uploaded',
            'image6_uploaded',
            'image7_uploaded',
            #'owner',
            #'id_vehicle',
            'original_type',
            'final_type',
        )

class imagenesPrueba(forms.Form):
    image1_uploaded = forms.ImageField(label="prueba1")
    image2_uploaded = forms.ImageField(label="Foto Frente")
    image3_uploaded = forms.ImageField(label="Foto lateral 1")
