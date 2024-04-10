from django.shortcuts import render
from django.http import HttpResponse

from appEmpresaDjango.models import Empleado, Departamento, Habilidad


# Create your views here.
def index_departamentos(request):
    departamentos = Departamento.objects.all()
    output = ', '.join([d.nombre for d in departamentos])
    return HttpResponse(output)


def show_departamento(request, departamento_id):
    departamento = Departamento.objects.get(id=departamento_id)
    output = f'Detalles del departamento: {departamento.id}, {departamento.nombre}, {departamento.telefono}'
    return HttpResponse(output)


# devuelve los empleados asociados a un departamento
def index_empleados(request, departamento_id):
    departamento = Departamento.objects.get(pk=departamento_id)
    salida = ", ".join([e.nombre for e in departamento.empleado_set.all()])
    return HttpResponse(salida)


def show_empleado(request, empleado_id):
    empleado = Empleado.objects.get(pk=empleado_id)
    output = f'Detalles del empleado: {empleado.id}, {empleado.nombre}, {empleado.fecha_nacimiento}, {empleado.antiguedad},{str(empleado.departamento)}, Habilidades: {[h.nombre for h in empleado.habilidad.all()]}'
    return HttpResponse(output)

def show_habilidad(request, habilidad_id):
    habilidad = Habilidad.objects.get(pk=habilidad_id)
    output = (f'Detalles de la habilidad: {habilidad.id}, {habilidad.nombre},'
              f' Empleados :{[e.nombre for e in habilidad.empleado_set.all()]}')
    return HttpResponse(output)