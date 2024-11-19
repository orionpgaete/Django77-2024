from django.core import validators
from django import forms

class Usuario (forms.Form) :
    
    ESTADOS =[('Valido', 'VALIDO'), ('invalido' , 'INVALIDO')] 

    nombre = forms.CharField(required=True)
    apellido = forms.CharField(validators=
                               [validators.MinLengthValidator(5),
                                validators.MaxLengthValidator(10)]

    )
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))

    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    password.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-select'
