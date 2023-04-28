from django.db import models
from Aplicacion1.models import Director


# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo