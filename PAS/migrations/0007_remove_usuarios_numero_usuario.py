# Generated by Django 4.0.3 on 2022-04-16 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PAS', '0006_remove_usuarios_apellido_materno_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='Numero_usuario',
        ),
    ]
