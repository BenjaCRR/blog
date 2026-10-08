from django.db import models

from django.db import models
from django.utils import timezone
class Tag(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    class Meta:
        ordering = ['nombre']
    def __str__(self):
        return self.nombre
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    fecha = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.CharField(max_length=80)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['fecha']

    def __str__(self):
        return f'{self.nombre} en {self.post}'