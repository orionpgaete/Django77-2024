from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'templateApp/index.html')

def datospersona(request):
    data = {"id" : "123456",
            "nombre" : "Pedro Gaete", 
            "email": "pedro.gaete@inacapmail.cl"}
    return render(request, 'templateApp/primeraweb.html', data)


