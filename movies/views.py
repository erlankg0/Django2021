from django.shortcuts import render
from django.views.generic import View

from movies.models import Movie


class MovieView(View):
    """ Список фильмов """

    def get(self, request):
        movies = Movie.objects.all()  # SELECT * FROM movies_movie
        data = {'movies': movies}
        return render(request, 'movies/movies.html', context=data)
