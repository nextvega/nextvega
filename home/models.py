from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Modelo de post o news para el blog.
class CustomUser(AbstractUser):
    token = models.CharField(max_length=60, unique= True, verbose_name='Token:', blank=True, null=True)

class EntryBlog(models.Model):
    nombre_noticia = models.CharField(max_length=60, verbose_name='Nombre:', default='')
    preview_noticia = models.TextField(max_length=250, verbose_name='Subnombre:', default='')
    autor_noticia = models.CharField(max_length=60, verbose_name='Autor:', default='')
    slug_noticia = models.CharField(max_length=60, verbose_name='Url Amigable', default='', editable=False)
    image_noticia = models.ImageField(upload_to='news_images/', blank=True, null=True)
    text = CKEditor5Field('Text', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El :')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El :')

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entry's"

    def clean(self):
        url = self.nombre_noticia.lower()  
        self.slug_noticia = url.replace(" ", "-")

    def __str__(self):
        return f'{self.nombre_noticia}'
    
# Modelo de comentarios para el post o news.
class ComentariosBlog(models.Model):
    autor_comentario = models.CharField(max_length=100)
    contenido_comentario = models.TextField(verbose_name='Contenido:')
    noticia_comentario = models.ForeignKey(EntryBlog, on_delete=models.CASCADE, related_name='entryblog')
    comentario_padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='respuestas', verbose_name='Comentario Relacion:', limit_choices_to={'primario': True})
    primario = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El :')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El :')

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return f"Comentario por : {self.autor_comentario}"