from django import forms

class FormLogin(forms.Form):
    id_number = forms.CharField(label="DNI", required=True)
    domain = forms.CharField(label="Patente", required=True)

class FormDoc(forms.Form):
    id_number = forms.CharField(label="DNI", required=True)
    domain = forms.CharField(label="Patente", required=True)