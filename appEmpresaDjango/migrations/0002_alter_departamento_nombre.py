# Generated by Django 4.2.11 on 2024-03-20 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEmpresaDjango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
    ]
