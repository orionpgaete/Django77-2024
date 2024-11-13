from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    form = forms.Usuario()

    if request.method == 'POST':
        form = forms.Usuario(request.POST)
        if form.is_valid():
            print ("DATOS OK!!!!")
            print ("Nombre : " , form.cleaned_data['nombre'])
            print ("Email : " , form.cleaned_data['email'])
       
    data = {'form' : form}
    return render (request, 'index.html', data)
    