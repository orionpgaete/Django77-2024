from django.shortcuts import render
from ProyectoAPP_2.models import Clientes

# Create your views here.

def index(request):
    return render(request, 'index.html')

def clientedata(request):
    cliente = Clientes.objects.all()
    data = {'clienteweb' : cliente}
    return render(request, 'cliente.html', data)