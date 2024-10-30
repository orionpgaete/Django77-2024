from django.shortcuts import redirect, render
from ProyectoAPP_3.models import Persona
from ProyectoAPP_3.forms import FormPersona

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listaPersona(request):
    persona = Persona.objects.all()
    data = {'perso': persona}
    return render(request, 'ListarPersonas.html', data)

def agregarPersona(request):
    form = FormPersona()

    if request.method == 'POST' :
        form = FormPersona(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    
    data = {'formP' : form}
    return render(request, 'agregarPersona.html', data)


def eliminarPersona(request, id):
    perso = Persona.objects.get(id = id)
    perso.delete()
    return redirect('/listarP')

def actualizarPersona(request, id):
    perso = Persona.objects.get(id = id)
    form = FormPersona(instance=perso)
    
    if request.method == 'POST':
        form = FormPersona(request.POST, instance=perso)
        if form.is_valid() :
            form.save()
        return index(request)
    
    data = {'formP' : form}
    return render(request, 'agregarPersona.html', data)