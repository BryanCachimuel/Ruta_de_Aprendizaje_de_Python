from django.db import models

# importando ckeditor
from ckeditor.fields import RichTextField

# Create your models here.
# verbose_name sirve para traducir los nombres de los campos para que se vean en español en el panel de administración
class Post(models.Model):
    image = models.ImageField(verbose_name='Imagen', upload_to='blog')
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    content = RichTextField(verbose_name='Contenido')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    # Traduce los subititulos de cada sección de las aplicaciones 
    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        # forma de ordenar los registros
        ordering = ['-created']

    def __str__(self):
        return self.title
