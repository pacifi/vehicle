# Generated by Django 5.1.3 on 2024-11-11 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applica', '0007_soat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='soat',
            old_name='fecha_actualizacion',
            new_name='fecha_renovacion',
        ),
    ]