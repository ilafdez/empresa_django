from django.shortcuts import render
from django.http import HttpResponse

from appEmpresaDjango.models import Empleado

# Create your views here.
def index(request):
    return HttpResponse("Hello World")
def list(request):
    empleados = Empleado.objects.all()
    salida = ", ".join([e.nombre for e in empleados])
    return HttpResponse(salida)