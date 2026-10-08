from django.contrib import admin
from .models import Post, Comentario, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    filter_horizontal = ('tags',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'post', 'fecha')
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('nombre',)