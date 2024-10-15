from django.shortcuts import render
from ProyectoAPP_3.models import Persona
from ProyectoAPP_3.forms import FormPersona

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listaPersona(request):
    persona = Persona.objects.all()
    data = {'perso': persona}
    return render(request, 'listapersonas.html', data)

def agregarPersona(request):
    form = FormPersona()

    data = {'formP' : form}
    return render(request, 'agregarPersona.html', data)
