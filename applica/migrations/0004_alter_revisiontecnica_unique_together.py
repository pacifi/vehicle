# Generated by Django 5.1.3 on 2024-11-08 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applica', '0003_alter_conductor_dni'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='revisiontecnica',
            unique_together={('vehiculo',)},
        ),
    ]
