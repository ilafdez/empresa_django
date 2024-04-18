"""
URL configuration for empresaDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import DepartamentoListView, DepartamentoDetailView, EmpleadoListView, EmpleadoDetailView, \
    DepartamentoCreateView, EmpleadoCreateView

urlpatterns = [
    #path('/',views.index_departamentos, name="index" ),
    path('/', DepartamentoListView.as_view(), name='index'),
    #path('/departamentos/<int:departamento_id>',views.show_departamento, name="departamentos_show"),
    path('/departamentos/<int:pk>', DepartamentoDetailView.as_view(), name='departamentos_show'),
    #path('/departamentos/<int:departamento_id>/empleados', views.index_empleados, name="empleados_index"),
    path('/departamentos/<int:departamento_id>/empleados', EmpleadoListView.as_view(), name='empleados_index'),
    #path('/empleados/<int:empleado_id>', views.show_empleado, name="empleados_show"),
    path('/empleados/<int:pk>', EmpleadoDetailView.as_view(), name="empleados_show"),
    path('/habilidades/<int:habilidad_id>', views.show_habilidad, name="habilidades_show"),

    path('/departamentos/create', DepartamentoCreateView.as_view(), name='departamento_create'),
    path('/empleados/create', EmpleadoCreateView.as_view(),name="empleado_create")
    #prueba de error 500
    #path('/error', views.probar_error, name="error")
]
