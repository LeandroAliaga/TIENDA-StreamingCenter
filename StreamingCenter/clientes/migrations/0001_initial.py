# Generated by Django 4.0.4 on 2022-06-07 21:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.CharField(default=uuid.UUID('fa451636-52c8-4e16-9fb7-dbc8912a4846'), max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('fechaVencimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=30)),
                ('servicio', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.CharField(default=uuid.UUID('3372d641-4a1f-49e5-bf9c-dd3845a59176'), max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('area', models.CharField(blank=True, choices=[('ATENCION AL CLIENTE', 'ATENCION AL CLIENTE'), ('ADMINISTRACION', 'ADMINISTRACION'), ('PROGRAMADOR', 'PROGRAMADOR')], max_length=30, null=True)),
                ('antiguedad_meses', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.CharField(default=uuid.UUID('2f17d1dc-3256-43cc-9c17-d8f1723c839d'), max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
