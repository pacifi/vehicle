# Generated by Django 5.1.3 on 2024-11-08 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductor',
            name='dni',
            field=models.CharField(default=123, max_length=8, unique=True),
            preserve_default=False,
        ),
    ]
