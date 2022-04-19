from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Canciones(models.Model):
    Nombre= models.CharField(max_length=50)
    Duracion = models.CharField(max_length=30)
    Genero= models.CharField(max_length=30)
    Ritmo= models.CharField(max_length=30)
    Dificultad = models.CharField(max_length=30)

class Usuarios(models.Model):
    Contraseña= models.CharField(max_length=50, default='1')
    Nombre_usuario= models.CharField(max_length=50)
    nombre_principal = models.CharField(max_length=30)
    Pais = models.CharField(max_length=30)

class Historial(models.Model):
    Nombre_usuario= models.CharField(max_length=50)
    #Nombre_usuario= models.CharField(Usuarios, on_delete=models.CASCADE)
    ID_Usuarios= models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    Puntos_por_partida= models.CharField(max_length=30)
    Fecha_del_juego= models.CharField(max_length=30)
    ID_Canciones= models.ForeignKey(Canciones, on_delete=models.CASCADE)
    Tiempo_jugado = models.CharField(max_length=30)
    

