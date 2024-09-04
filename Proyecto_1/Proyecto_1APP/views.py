from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    data = {"id" : "123456",
            "nombre" : "Pedro Gaete", 
            "email": "pedro.gaete@inacapmail.cl"}
    return render(request, 'templateApp/primeraweb.html', data)