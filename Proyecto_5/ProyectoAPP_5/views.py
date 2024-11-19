from django.http import JsonResponse
from django.shortcuts import render
from ProyectoAPP_5.models import Persona 

# Create your views here.

def empleados (request):

    emp = {
        'id' : 1234,
        'nombre' : 'Pedro',
        'email' : 'pedro@inacap.cl',
        'sueldo' : 1000000000
    }

    return JsonResponse(emp)


def empleadosDB(resquest):

    empleados = Persona.objects.all()
    data = {'emple' : list(empleados.values('nombre', 'apellido', 'email'))}

    return JsonResponse(data)
