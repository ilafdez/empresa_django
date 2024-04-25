from django import forms

from appEmpresaDjango.models import Departamento, Empleado


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        #fields = ['nombre','telefono']
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        #fields = ['nombre','fecha_nacimiento','antiguedad','departamento','habilidad']
        fields='__all__'