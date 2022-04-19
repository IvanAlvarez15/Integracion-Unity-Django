from django.contrib import admin
from .models import Usuarios, Canciones, Historial
# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Canciones)
admin.site.register(Historial)