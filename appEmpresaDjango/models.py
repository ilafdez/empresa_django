from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=60)
    telefono =  models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.nombre} ({self.telefono})"

    class Meta:
        verbose_name_plural = "departamentos"
        verbose_name= "departamento"
        ordering = ["-created"]

class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "habilidades"
        verbose_name = "habilidad"
        ordering = ["-created"]


class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_nacimiento=models.DateField()
    antiguedad=models.IntegerField()
    departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE) #1-N
    habilidad= models.ManyToManyField(Habilidad) #N-M
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.nombre} --- {self.antiguedad}"

    class Meta:
        verbose_name_plural = "empleados"
        verbose_name= "empleado"
        ordering = ["-created"]