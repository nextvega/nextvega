from django.contrib import admin
from .models import EntryBlog, ComentariosBlog, CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class EntryBlogAdmin(admin.ModelAdmin):
    readonly_fields = ('slug_noticia', )
    search_fields=('nombre_noticia', 'preview_noticia')
    list_filter=('created_at','updated_at')
    list_per_page = 15
    date_hierarchy= 'created_at'
    list_display=( 
        'nombre_noticia',
        'preview_noticia',
        'created_at',
    )

class ComentariosBlogAdmin(admin.ModelAdmin):
    search_fields=('autor_comentario', 'created_at')
    list_filter=('primario', 'created_at','updated_at')
    list_per_page = 15
    date_hierarchy= 'created_at'
    list_display=( 
        'autor_comentario',
        'created_at',
    )
    
admin.site.register(EntryBlog, EntryBlogAdmin)
admin.site.register(ComentariosBlog, ComentariosBlogAdmin)
admin.site.register(CustomUser, UserAdmin)