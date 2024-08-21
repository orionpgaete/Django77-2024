import datetime
from django.http import HttpResponse

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
