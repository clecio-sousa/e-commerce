from django.contrib import admin
from .models import Usuario

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')

admin.site.register(Usuario, UsuarioAdmin)