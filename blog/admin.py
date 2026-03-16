from django.contrib import admin
from .models import Autor, Categoria, Post


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email', 'fecha_registro']
    search_fields = ['nombre', 'apellido', 'email']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'categoria', 'estado', 'fecha_creacion']
    list_filter = ['estado', 'categoria']
    search_fields = ['titulo', 'contenido']
    list_editable = ['estado']
