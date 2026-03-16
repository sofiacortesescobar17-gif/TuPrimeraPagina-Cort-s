from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(unique=True, verbose_name="Email")
    bio = models.TextField(blank=True, verbose_name="Biografía")
    fecha_registro = models.DateField(auto_now_add=True, verbose_name="Fecha de registro")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['apellido', 'nombre']


class Categoria(models.Model):
    nombre = models.CharField(max_length=80, unique=True, verbose_name="Nombre")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    color = models.CharField(
        max_length=7,
        default='#6366f1',
        verbose_name="Color (HEX)",
        help_text="Ej: #FF5733"
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']


class Post(models.Model):
    ESTADO_CHOICES = [
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título")
    contenido = models.TextField(verbose_name="Contenido")
    resumen = models.CharField(max_length=300, blank=True, verbose_name="Resumen")
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Autor"
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name="Categoría"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name="Última modificación")
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='borrador',
        verbose_name="Estado"
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-fecha_creacion']
