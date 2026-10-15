from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (('Datos adicionales', {'fields': ('documento',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (('Datos adicionales', {'fields': ('documento',)}),)

# Register your models here.