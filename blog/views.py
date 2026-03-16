from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Autor, Categoria, Post
from .forms import AutorForm, CategoriaForm, PostForm, BuscarPostForm


# ───────────────────────────── HOME ─────────────────────────────

def home(request):
    posts_recientes = Post.objects.filter(estado='publicado').order_by('-fecha_creacion')[:6]
    total_posts = Post.objects.filter(estado='publicado').count()
    total_autores = Autor.objects.count()
    total_categorias = Categoria.objects.count()
    context = {
        'posts': posts_recientes,
        'total_posts': total_posts,
        'total_autores': total_autores,
        'total_categorias': total_categorias,
    }
    return render(request, 'blog/home.html', context)


# ───────────────────────────── POSTS ─────────────────────────────

def lista_posts(request):
    posts = Post.objects.filter(estado='publicado').order_by('-fecha_creacion')
    categorias = Categoria.objects.all()
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        posts = posts.filter(categoria_id=categoria_id)
    context = {
        'posts': posts,
        'categorias': categorias,
        'categoria_activa': categoria_id,
    }
    return render(request, 'blog/lista_posts.html', context)


def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html', {'post': post})


def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, f'✅ Post "{post.titulo}" creado correctamente.')
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'blog/form_post.html', {'form': form, 'accion': 'Crear'})


def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f'✅ Post "{post.titulo}" actualizado.')
            return redirect('lista_posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/form_post.html', {'form': form, 'accion': 'Editar', 'post': post})


def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        titulo = post.titulo
        post.delete()
        messages.success(request, f'🗑️ Post "{titulo}" eliminado.')
        return redirect('lista_posts')
    return render(request, 'blog/confirmar_eliminar.html', {'objeto': post, 'tipo': 'Post'})


# ───────────────────────────── AUTORES ─────────────────────────────

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'blog/lista_autores.html', {'autores': autores})


def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save()
            messages.success(request, f'✅ Autor "{autor.nombre_completo()}" creado correctamente.')
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'blog/form_autor.html', {'form': form, 'accion': 'Crear'})


def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, f'✅ Autor "{autor.nombre_completo()}" actualizado.')
            return redirect('lista_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'blog/form_autor.html', {'form': form, 'accion': 'Editar', 'autor': autor})


def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        nombre = autor.nombre_completo()
        autor.delete()
        messages.success(request, f'🗑️ Autor "{nombre}" eliminado.')
        return redirect('lista_autores')
    return render(request, 'blog/confirmar_eliminar.html', {'objeto': autor, 'tipo': 'Autor'})


# ───────────────────────────── CATEGORÍAS ─────────────────────────────

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'blog/lista_categorias.html', {'categorias': categorias})


def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            cat = form.save()
            messages.success(request, f'✅ Categoría "{cat.nombre}" creada correctamente.')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'blog/form_categoria.html', {'form': form, 'accion': 'Crear'})


def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, f'✅ Categoría "{categoria.nombre}" actualizada.')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'blog/form_categoria.html', {
        'form': form, 'accion': 'Editar', 'categoria': categoria
    })


def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        nombre = categoria.nombre
        categoria.delete()
        messages.success(request, f'🗑️ Categoría "{nombre}" eliminada.')
        return redirect('lista_categorias')
    return render(request, 'blog/confirmar_eliminar.html', {'objeto': categoria, 'tipo': 'Categoría'})


# ───────────────────────────── BÚSQUEDA ─────────────────────────────

def buscar_post(request):
    form = BuscarPostForm(request.GET or None)
    resultados = None
    query = ''

    if form.is_valid():
        query = form.cleaned_data['query']
        resultados = Post.objects.filter(
            titulo__icontains=query
        ) | Post.objects.filter(
            contenido__icontains=query
        )
        resultados = resultados.distinct().order_by('-fecha_creacion')

    context = {
        'form': form,
        'resultados': resultados,
        'query': query,
    }
    return render(request, 'blog/buscar.html', context)
