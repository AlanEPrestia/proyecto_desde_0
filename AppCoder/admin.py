from django.contrib import admin
from .models import Estudiante, Profesor, Curso, Entregable

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Entregable)

class UserAdmin(BaseUserAdmin): 
    # Define las columnas que se mostrarán en la lista de usuarios en el panel de administración de Django. 
    # En este caso, se mostrarán: nombre de usuario, email, nombre, apellido
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # Permite buscar usuarios en el panel de administración usando los campos especificados (nombre de usuario, nombre, apellido y email)
    search_fields = ('username', 'first_name', 'last_name', 'email')
    # Hace que los campos listados sean de solo lectura en el formulario de edición del usuario
    readonly_fields = ('date_joined', 'last_login')
    # Organiza los campos del formulario de edición en secciones
    fieldsets = (
        ('Usuario - Contraseña', {'fields': ('username', 'password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    ) 
admin.site.unregister(User) 
admin.site.register(User, UserAdmin)