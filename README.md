# TuPrimeraPagina + [TuApellido]

Proyecto Web en Django con patrón MVT — Blog de artículos con autores y categorías.

---

## 📋 Descripción

Blog desarrollado con Django que incluye:

- **Herencia de plantillas HTML** (`base.html` como padre de todas las vistas)
- **3 modelos**: `Autor`, `Categoria`, `Post`
- **Formularios de inserción** para cada modelo
- **Formulario de búsqueda** de posts por título y contenido
- Panel de administración Django

---

## 🗂️ Estructura del proyecto

```
TuPrimeraPaginaBlog/
├── blog/
│   ├── admin.py          # Registro en panel admin
│   ├── forms.py          # AutorForm, CategoriaForm, PostForm, BuscarPostForm
│   ├── models.py         # Autor, Categoria, Post
│   ├── urls.py           # URLs de la app
│   └── views.py          # Vistas (lógica MVT)
├── miblog/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
│   └── blog/
│       ├── base.html              ← Plantilla padre (herencia)
│       ├── home.html              ← Hereda de base.html
│       ├── lista_posts.html       ← Hereda de base.html
│       ├── detalle_post.html      ← Hereda de base.html
│       ├── form_post.html         ← Hereda de base.html
│       ├── lista_autores.html     ← Hereda de base.html
│       ├── form_autor.html        ← Hereda de base.html
│       ├── lista_categorias.html  ← Hereda de base.html
│       ├── form_categoria.html    ← Hereda de base.html
│       ├── buscar.html            ← Hereda de base.html
│       └── confirmar_eliminar.html
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/TuPrimeraPaginaApellido.git
cd TuPrimeraPaginaApellido
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv

# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Crear superusuario (opcional, para el admin)

```bash
python manage.py createsuperuser
```

### 5. Correr el servidor

```bash
python manage.py runserver
```

Abrir en el navegador: **http://127.0.0.1:8000/**

---

## 🧭 Orden para probar las funcionalidades

### Paso 1 — Crear una Categoría
- Ir a: **http://127.0.0.1:8000/categorias/nueva/**
- O desde la navbar: **Nuevo → Nueva Categoría**
- Completar nombre, descripción y color
- ✅ Esto carga datos al modelo `Categoria`

### Paso 2 — Crear un Autor
- Ir a: **http://127.0.0.1:8000/autores/nuevo/**
- O desde la navbar: **Nuevo → Nuevo Autor**
- Completar nombre, apellido, email y biografía
- ✅ Esto carga datos al modelo `Autor`

### Paso 3 — Crear un Post
- Ir a: **http://127.0.0.1:8000/posts/nuevo/**
- O desde la navbar: **Nuevo → Nuevo Post**
- Seleccioná el autor y categoría creados en los pasos anteriores
- Cambiar estado a "Publicado" para que aparezca en el home
- ✅ Esto carga datos al modelo `Post`

### Paso 4 — Buscar Posts
- Ir a: **http://127.0.0.1:8000/buscar/**
- O desde la navbar: **Buscar**
- Ingresar palabras del título o contenido del post
- ✅ Muestra resultados filtrados desde la BD (búsqueda sobre el modelo `Post`)

### Paso 5 — Explorar el blog
- **Home**: http://127.0.0.1:8000/ — Estadísticas y posts recientes
- **Posts**: http://127.0.0.1:8000/posts/ — Lista con filtro por categoría
- **Autores**: http://127.0.0.1:8000/autores/ — Lista de autores
- **Categorías**: http://127.0.0.1:8000/categorias/ — Lista de categorías

### Paso 6 — Panel de administración
- Ir a: **http://127.0.0.1:8000/admin/**
- Iniciar sesión con el superusuario creado

---

## 📌 Funcionalidades implementadas

| Funcionalidad | URL | Descripción |
|---|---|---|
| Inicio | `/` | Home con stats y posts recientes |
| Lista Posts | `/posts/` | Ver todos los posts, filtrar por categoría |
| Detalle Post | `/posts/<id>/` | Ver post completo |
| **Crear Post** | `/posts/nuevo/` | **Formulario de inserción** |
| Editar Post | `/posts/<id>/editar/` | Modificar post existente |
| Eliminar Post | `/posts/<id>/eliminar/` | Eliminar con confirmación |
| Lista Autores | `/autores/` | Ver todos los autores |
| **Crear Autor** | `/autores/nuevo/` | **Formulario de inserción** |
| Editar Autor | `/autores/<id>/editar/` | Modificar autor |
| Lista Categorías | `/categorias/` | Ver todas las categorías |
| **Crear Categoría** | `/categorias/nueva/` | **Formulario de inserción** |
| Editar Categoría | `/categorias/<id>/editar/` | Modificar categoría |
| **Buscar Posts** | `/buscar/` | **Formulario de búsqueda en BD** |
| Admin | `/admin/` | Panel de administración Django |

---

## 🏗️ Modelos

### `Autor`
| Campo | Tipo |
|---|---|
| nombre | CharField |
| apellido | CharField |
| email | EmailField (único) |
| bio | TextField |
| fecha_registro | DateField (auto) |

### `Categoria`
| Campo | Tipo |
|---|---|
| nombre | CharField (único) |
| descripcion | TextField |
| color | CharField (HEX) |

### `Post`
| Campo | Tipo |
|---|---|
| titulo | CharField |
| contenido | TextField |
| resumen | CharField |
| autor | ForeignKey → Autor |
| categoria | ForeignKey → Categoria |
| fecha_creacion | DateTimeField (auto) |
| estado | CharField (borrador/publicado) |

---

## 🧩 Herencia de Plantillas

Todas las páginas heredan de `templates/blog/base.html` usando:

```html
{% extends "blog/base.html" %}

{% block title %}Título de la página{% endblock %}

{% block content %}
  <!-- Contenido específico de cada página -->
{% endblock %}
```

`base.html` define: navbar, sistema de mensajes, footer y todos los estilos globales.

---

*Proyecto para CoderHouse — Curso Django*
