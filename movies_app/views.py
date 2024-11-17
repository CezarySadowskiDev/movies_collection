from django.shortcuts import render
from .models import Movies


def get_movies_from_db():
    movies = Movies.objects.all()
    return movies


def get_movie_from_db_by_slug(slug):
    movie = Movies.objects.get(slug=slug)
    return movie


def index(request):
    movies = get_movies_from_db()
    return render(request, "movies_app/index.html", {
        "movies": movies
    })


def movie_details_page(request, slug):
    movie = get_movie_from_db_by_slug(slug)

    return render(request, "movies_app/movie_details_page.html", {
        "movie": movie
    })
