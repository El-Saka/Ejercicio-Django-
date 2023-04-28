from django.db import models

# Create your models here.

class Director(models.Model):
    objects = None
    nombre = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.nombre


class Pelicula:
    pass