from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import sqlite3
from .models import Canciones, Usuarios, Historial
from .forms import CambiarPassword
from django.contrib.auth.views import LogoutView
from django.views.decorators.csrf import csrf_exempt #excepcion POST
import ast #para diccionario
import json
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
#from .forms import RegisterUserForm
# Create your views here.
def Sobrejuego(request):
    return render(request, 'PAS/about-game.html', {})

def Cambiarcontra(request, id): #Ya se actualiza la contraseña
    if request.method == 'POST':
        Intento1 = request.POST['Contraseña']
        Intento2 = request.POST['Confirmacion']
        if Intento1 == Intento2:
            u = User.objects.get(id = id)
            u.set_password(Intento1)
            u.save()
            return render(request, 'PAS/index.html', {})
        else:
            return render(request, 'PAS/change-pass.html', {"user":temp_user})
        #return render(request, 'PAS/index.html', {})
    else:
        temp_user = Usuarios.objects.get(Numero_usuario = id)
        #temp_user = User.objects.get(id = id)
        return render(request, 'PAS/change-pass.html', {"user":temp_user})

def editarperfil(request, id): # Errores detectados
    if request.user.is_authenticated and request.method != "POST":
        temp_user = Usuarios.objects.get(Numero_usuario = id)
        #print(temp_user.Nombre_usuario) #Si selecciona el perfil correcto
        return render(request, 'PAS/edit-profile.html', {"user":temp_user}) # paso id -> "id": 
    elif request.user.is_authenticated and request.method == 'POST':
        Num=request.POST['uid'] #Recibe 4 en lugar del numero real (5) en este caso, pasa lo mismo en los demás casos de cambio
        usuario_nuevo = request.POST['nombre']
        Fecha_nueva = request.POST['Fecha']
        Apellido_nuevo = request.POST['Apellido']
        Pais_nuevo = request.POST['Pais']
        genero_nuevo = request.POST['Gender']
        tel_nuevo = request.POST['Numero']
        Apellido_nuevo_2 = request.POST['Apellido2']
        print(Pais_nuevo) #Si lo imprime en la terminal
        user_temp= Usuarios.objects.get(Numero_usuario = Num) #UPDATE #No siempre selecciona algo # El error esta en esta linea
        print(user_temp)
        user_temp.Pais = Pais_nuevo
        user_temp.Fecha_nacimiento = Fecha_nueva
        user_temp.nombre_principal = usuario_nuevo
        user_temp.Apellido_paterno = Apellido_nuevo
        user_temp.Genero = genero_nuevo
        user_temp.Telefono = tel_nuevo
        user_temp.Apellido_materno = Apellido_nuevo_2
        user_temp.save()
        return render(request, 'PAS/index.html', {})
        #us.update(nombre_principal = usuario_nuevo)
        # cur.execute("SELECT * FROM tasks") #Aqui la querry
        # Model.objects.filter(id = 223).update(field1 = 2)
    else:
        return render(request, 'PAS/index.html', {})

def Comojugar(request):#Ya quedo
    return render(request, 'PAS/how-to-play.html', {})

def index(request):#Ya quedo
    return render(request, 'PAS/index.html', {})

def registrarse(request): #Se leen los datos de manera correcta pero hay un error en el mensaje que se muestra
    if request.method == 'POST':
        usuario = request.POST['usuario'] 
        Contra = request.POST['Contraseña']
        user = authenticate(request, username=usuario, password=Contra)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, ('El nombre de usuario o la contraseña pueden estar incorretos, ingreselos nuevamente'))
            return redirect('Registrarse')        
    else:
        return render(request, 'PAS/log-in.html', {})

def ourteam(request): #Esta lista
    return render(request, 'PAS/our-team.html', {})

def ingresar(request): # Ya quedo
    if request.method == 'POST': #CREATE
        usuario = request.POST['Usuario']
        nombre = request.POST['nombre']
        Fecha = request.POST['Fecha']
        Contra = request.POST['Contra']
        mail = ""
        Apellido1 = request.POST['Apellido']
        Gender = request.POST['Gender']
        Apellido2 = request.POST['Apellido2']
        Pais = request.POST['Pais']
        numero = request.POST['Numero']
        user = User.objects.create_user(usuario,mail,Contra)
        user.save()
        user_temp= User.objects.get(username = usuario)
        #print(user_temp)
        p= Usuarios(Nombre_usuario=usuario, Pais=Pais, Fecha_nacimiento=Fecha, Apellido_materno=Apellido2, Apellido_paterno=Apellido1, Genero=Gender, Telefono=numero,Foto='', Status='',nombre_principal=nombre, Numero_usuario = user_temp.id)
        p.save()
        return redirect('Estadisticas_personales')
    else:
        return render(request, 'PAS/sign-in.html', {})

def estadisticasglobales(request):
    return render(request, 'PAS/stadistics-global.html', {})

def estadisticaspersonales(request):
    if request.user.is_authenticated:
        return render(request, 'PAS/stadistics-personal.html', {})
    else:
        return render(request, 'PAS/index.html', {})

def logout_user(request):#Ya quedo
    logout(request)
    #messages.success(request, ('Logged out'))
    return redirect('index')

def Borrar(request, id):#Ya quedo
    if request.method == 'POST':
        temp_user = Usuarios.objects.get(Numero_usuario = id)
        temp_user.delete()
        #success_url = reverse_lazy('index')
        temp_user2 = User.objects.get(id = id)
        temp_user2.delete()
        return render(request, 'PAS/index.html',{})
    else:
        temp_user = User.objects.get(id = id)
        return render(request, 'PAS/Borrar.html', {"user":temp_user})


@csrf_exempt#Este código sirve para comunicarse entre Django y UNITY
def Conexion(request): #Esto es el de consulta
    if request.method == 'POST':
        var = request.body #viene de Unity
        dicc=ast.literal_eval(var.decode('utf-8'))
        print(var)
        print(dicc)
        u = Usuarios.objects.filter(Nombre_usuario = dicc['id'])
        jsonnuevo = (request.body).decode()
        jsonnuevo = json.loads(jsonnuevo)
        print(u)
        if u=={} or len(u) == 0:
            print("Malo")
            return HttpResponse("No se encuentra") #No se encontró nada
        else: 
            n = Usuarios.objects.get(Nombre_usuario = dicc['id'])
            if n.Contraseña != dicc['title']:
                print("Mala contraseña")
                return HttpResponse("No se encuentra") #No se encontró nada
            else: #Esta regresando esto 
                print("Encontrado")
                #print(n.Pais)
                return JsonResponse(jsonnuevo) #Le regresa a unity lo que esta dentro de var
    else:
        return HttpResponse("Please use post")

@csrf_exempt#Este código sirve para comunicarse entre Django y UNITY
def Conexionregistro(request):#Ese es el de alta
    if request.method == 'POST':
        var = request.body #viene de Unity
        dicc=ast.literal_eval(var.decode('utf-8'))
        print(var)
        p=Usuarios(Nombre_usuario = dicc['id'], Pais = dicc['userId'], nombre_principal = dicc['body'], Contraseña = dicc['title'])
        p.save()
        u=Usuarios.objects.filter(Nombre_usuario = dicc['id'])
        jsonnuevo = (request.body).decode()
        jsonnuevo = json.loads(jsonnuevo)
        if u=={} or len(u) == 0:
            return HttpResponse("No se encuentra") #No se encontró nada
        else: #Esta regresando esto 
            return JsonResponse(jsonnuevo) #Le regresa a unity lo que esta dentro de var
    else:
        return HttpResponse("Please use post")

@csrf_exempt#Este código sirve para comunicarse entre Django y UNITY
def ConexionCambio(request):#Este es el de cambio
    if request.method == 'POST':
        var = request.body #viene de Unity
        dicc=ast.literal_eval(var.decode('utf-8'))
        print(var)
        u=Usuarios.objects.get(Nombre_usuario = dicc['id'])
        if u=={}:
            return HttpResponse("No se encuentra") #No se encontró nada
        else: #Esta regresando esto 
            u.Nombre_usuario = dicc['id']
            u.Pais = dicc['userId']
            u.nombre_principal = dicc['body']
            u.Contraseña = dicc['title']
            u.save()
            jsonnuevo = (request.body).decode()
            jsonnuevo = json.loads(jsonnuevo)
            return JsonResponse(jsonnuevo) #Le regresa a unity lo que esta dentro de var
    else:
        return HttpResponse("Please use post")
