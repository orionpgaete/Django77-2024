from django import forms
from ProyectoAPP_3.models import Persona

class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
