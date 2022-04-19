from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name="index"),
    path('index/', views.index, name="index"),
    path('Cambiar_contraseña/', views.Cambiarcontra, name="Cambiar"),
    path('Cambiar_contraseña/<int:id>', views.Cambiarcontra, name="Cambiar"),
    path('Editar_perfil/', views.editarperfil, name="Editar_perfil"),
    path('Editar_perfil/<int:id>', views.editarperfil, name="Editar_perfil"),
    path('Como_jugar/', views.Comojugar, name="Como_jugar"),
    path('Sobre_juego/', views.Sobrejuego, name="Sobre_juego"),
    path('Registrarse/', views.registrarse, name="Registrarse"),
    path('Nuestro_equipo/', views.ourteam, name="Nuestro_equipo"),
    path('Ingresar/', views.ingresar, name="Ingresar"),
    path('Estadisticas_globales/', views.estadisticasglobales, name="Estadisticas_globales"),
    path('Estadisticas_personales/', views.estadisticaspersonales, name="Estadisticas_personales"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('Borrar/', views.Borrar, name="Borrar"),
    path('Borrar/<int:id>', views.Borrar, name="Borrar"),
    #Conexion a UNITY
    path('Conexion/', views.Conexion, name="Conexion"),
    path('Conexionregistro/', views.Conexionregistro, name="Conexionregistro"),
    path('ConexionCambio/', views.ConexionCambio, name="ConexionCambio"),
]