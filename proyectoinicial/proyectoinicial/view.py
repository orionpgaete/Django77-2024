import datetime
from django.http import HttpResponse

from django.template import Context, Template

def saluda(request):
    doc = """<html>
               <body>
                  <h1> Bienvenidos a la clase de Django </h1>
               </body>
              </html>  """
    
    return HttpResponse(doc)

def chaoo(request):
    return HttpResponse("Chaooo estas aprobado")

def fecha(request):
    fechahoy= datetime.datetime.now()

    doc = """<html>
               <body>
                  <h1> Fecha y hora actual es %s </h1>
               </body>
              </html>  """ % fechahoy
    
    return HttpResponse(doc)

def calculaedad(request, edad, agno):
    #edadactual=18
    periodo=agno-2024
    edadfutura=edad+periodo

    doc = "<html><body><h2> En el año %s tendras %s años" %(agno, edadfutura)

    return HttpResponse(doc)

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido = apellido

def saludoweb(request):

    p1 = Persona("Gonzalo", "Perez Bravo")
    #nombre="Pablo"

    #apellido="Perez Perez"

    temascurso=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]

    fechahoy= datetime.datetime.now()

    doc_externo = open("/Users/orion/Documents/1. Clases INACAP/2. Clases/2.31 Programacion Back-End/Proyecto 2024/proyectoinicial/proyectoinicial/plantilla/miplantilla.html")
    
    plt = Template(doc_externo.read()) 

    doc_externo.close()

    ctx = Context({"nombre_per":p1.nombre , "apellido_per":p1.apellido, "fechahoy":fechahoy, "temas":temascurso})

    document= plt.render(ctx)

    return HttpResponse(document)
