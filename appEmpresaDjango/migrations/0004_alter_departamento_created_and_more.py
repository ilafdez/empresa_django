# Generated by Django 4.2.11 on 2024-04-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEmpresaDjango', '0003_alter_departamento_options_alter_empleado_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]