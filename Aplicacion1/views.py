from django.shortcuts import render, get_object_or_404
from .models import Director, Pelicula

# Create your views here.

def lista_directores(request):
    directores = Director.objects.all()
    return render(request, 'directores/lista_directores.html', {'directores': directores})

def detalle_director(request, director_id):
    director = get_object_or_404(Director, pk=director_id)
    peliculas = director.pelicula_set.all()
    return render(request, 'directores/detalle_director.html', {'director': director, 'peliculas': peliculas})

def detalle_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
    return render(request, 'directores/detalle_pelicula.html', {'pelicula': pelicula})
