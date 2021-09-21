from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView, ListView

from movies.models import Movie


class MovieView(ListView):
    """ Список фильмов """
    queryset = Movie.objects.all()
    model = Movie
    template_name = 'movies/movies.html'
    context_object_name = 'movies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MovieView, self).get_context_data(**kwargs)
        context['last_movies'] = Movie.objects.order_by('year')
        return context


class MovieDetail(DetailView):
    """ Полное описание фильма """
    model = Movie
    slug_field = 'url'
    context_object_name = 'movie'
    template_name = 'movies/movie_detail.html'
