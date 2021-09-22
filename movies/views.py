from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, DetailView, ListView

from movies.models import Movie
from movies.forms import ReviewsForm


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


class AddReview(View):
    """ Отзывы """

    def post(self, request, pk):
        form = ReviewsForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect('/')
