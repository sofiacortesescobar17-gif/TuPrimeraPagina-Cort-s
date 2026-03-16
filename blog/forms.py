from django import forms
from .models import Autor, Categoria, Post


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'email', 'bio']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Juan'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: García'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@correo.com'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Contanos algo sobre vos...'
            }),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo Electrónico',
            'bio': 'Biografía',
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'color']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Tecnología'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción de la categoría...'
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control form-control-color',
                'type': 'color',
            }),
        }
        labels = {
            'nombre': 'Nombre de la Categoría',
            'descripcion': 'Descripción',
            'color': 'Color identificador',
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'resumen', 'contenido', 'autor', 'categoria', 'estado']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del post...'
            }),
            'resumen': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Un breve resumen (opcional)...'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,
                'placeholder': 'Escribí el contenido acá...'
            }),
            'autor': forms.Select(attrs={
                'class': 'form-select',
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select',
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
        labels = {
            'titulo': 'Título',
            'resumen': 'Resumen',
            'contenido': 'Contenido',
            'autor': 'Autor',
            'categoria': 'Categoría',
            'estado': 'Estado',
        }


class BuscarPostForm(forms.Form):
    query = forms.CharField(
        label='Buscar posts',
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscá por título o contenido...',
            'autofocus': True,
        })
    )
