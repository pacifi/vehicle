# Generated by Django 5.1.3 on 2024-11-08 01:58

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('licencia_conducir', models.CharField(max_length=50, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Incidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_incidencia', models.DateField(default=django.utils.timezone.now)),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(choices=[('Queja', 'Queja de Servicio'), ('Accidente', 'Accidente'), ('Otro', 'Otro tipo de incidencia')], max_length=100)),
                ('conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incidencias', to='applica.conductor')),
            ],
        ),
        migrations.CreateModel(
            name='Infraccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_infraccion', models.DateField()),
                ('descripcion', models.TextField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pagada', models.BooleanField(default=False)),
                ('conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infracciones', to='applica.conductor')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=20, unique=True)),
                ('anio', models.PositiveIntegerField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='applica.marca')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='applica.modelo')),
            ],
        ),
        migrations.CreateModel(
            name='RevisionTecnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_revision', models.DateField()),
                ('resultado', models.CharField(max_length=100)),
                ('observaciones', models.TextField(blank=True)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revisiones_tecnicas', to='applica.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='ExcesoVelocidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_evento', models.DateTimeField(default=django.utils.timezone.now)),
                ('velocidad', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ubicacion', models.CharField(max_length=200)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='excesos_velocidad', to='applica.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='ConductorVehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_asignacion', models.DateField(default=django.utils.timezone.now)),
                ('fecha_fin_asignacion', models.DateField(blank=True, null=True)),
                ('esta_activo', models.BooleanField(default=True)),
                ('conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applica.conductor')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applica.vehiculo')),
            ],
        ),
    ]
