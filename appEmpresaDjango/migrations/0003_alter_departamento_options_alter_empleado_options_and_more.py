# Generated by Django 4.2.11 on 2024-04-24 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appEmpresaDjango', '0002_alter_departamento_nombre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['-created'], 'verbose_name': 'departamento', 'verbose_name_plural': 'departamentos'},
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['-created'], 'verbose_name': 'empleado', 'verbose_name_plural': 'empleados'},
        ),
        migrations.AlterModelOptions(
            name='habilidad',
            options={'ordering': ['-created'], 'verbose_name': 'habilidad', 'verbose_name_plural': 'habilidades'},
        ),
    ]