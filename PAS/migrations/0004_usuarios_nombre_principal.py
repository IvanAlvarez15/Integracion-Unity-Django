# Generated by Django 4.0.3 on 2022-04-07 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PAS', '0003_remove_usuarios_contraseña'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='nombre_principal',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
