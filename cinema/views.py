import io
import os
import requests
from urllib.parse import urlparse
from PIL import Image

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from .forms import MovieForm
from .models import Movie


def movie_view(request, id):
    data = {
        'movie': Movie.objects.get(id=id)
    }
    return render(request, 'movie/movie-view.html', context=data, )


def movie_detail(request, id):
    movieReq = Movie.objects.get(id=id)
    movie = MovieForm(instance=movieReq)
    data = {
        'movieObject': movieReq,
        'form': movie
    }
    return render(request, 'movie/movie-detail.html', context=data, )


def index(request):
    data = {
        'movies': Movie.objects.all()
    }
    return render(request, 'index.html', context=data, )


def movie_delete(request, id):
    try:
        movie = Movie.objects.get(id=id)
        movie.delete()
        return HttpResponseRedirect('/cinema/index')
    except ObjectDoesNotExist:
        data = {
            'error': 'Película no encontrada'
        }
        return render(request, 'error-404.html', context=data, )


def movie_new(request):
    movie = MovieForm()
    data = {
        'form': movie
    }
    return render(request, 'movie/movie-detail.html', context=data, )


def url_web(url):
    global myimage
    response = requests.get(url)
    img = Image.open(io.BytesIO(response.content))
    parsed = urlparse(url)
    cadena = parsed.path
    posicion_barra = cadena.rfind('/')
    myimage = cadena[posicion_barra + 1:]
    location = '/static/img/'
    img.save(os.getcwd() + location + myimage)


def movie_save(request):
    global movie, img
    id_movie = request.POST.get('id')
    if id_movie == '':
        form = MovieForm(request.POST, request.POST.get('image_url'), request.FILES)
        if request.POST.get('image_url') != '':
            url = request.POST.get('image_url')
            url_web(url)
            form.instance.image = myimage
            form = MovieForm(request.POST)
        else:
            form = MovieForm(request.POST, request.FILES)
    else:
        id_movie = int(id_movie)
        movie = Movie.objects.get(id=id_movie)
        form = MovieForm(request.POST, request.POST.get('image_url'), request.FILES, instance=movie)
        if request.POST.get('image_url') != '':
            url = request.POST.get('image_url')
            url_web(url)
            movie.image = myimage
            form = MovieForm(request.POST, instance=movie)
        else:
            form = MovieForm(request.POST, request.FILES, instance=movie)
            movie.image = request.FILES.get('image')
    if not form.is_valid():
        return HttpResponseRedirect('/cinema/movie-new')
    location = 'static/img'
    path = os.path.join(location, str(request.FILES.get('image')))
    if os.path.exists(path):
        os.remove(path)
    movie = form.save()
    return redirect('movie-view', id=movie.id)
