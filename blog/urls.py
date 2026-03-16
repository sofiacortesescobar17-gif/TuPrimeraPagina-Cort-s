from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Posts
    path('posts/', views.lista_posts, name='lista_posts'),
    path('posts/<int:pk>/', views.detalle_post, name='detalle_post'),
    path('posts/nuevo/', views.crear_post, name='crear_post'),
    path('posts/<int:pk>/editar/', views.editar_post, name='editar_post'),
    path('posts/<int:pk>/eliminar/', views.eliminar_post, name='eliminar_post'),

    # Autores
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/nuevo/', views.crear_autor, name='crear_autor'),
    path('autores/<int:pk>/editar/', views.editar_autor, name='editar_autor'),
    path('autores/<int:pk>/eliminar/', views.eliminar_autor, name='eliminar_autor'),

    # Categorías
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/nueva/', views.crear_categoria, name='crear_categoria'),
    path('categorias/<int:pk>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categorias/<int:pk>/eliminar/', views.eliminar_categoria, name='eliminar_categoria'),

    # Búsqueda
    path('buscar/', views.buscar_post, name='buscar_post'),
]
