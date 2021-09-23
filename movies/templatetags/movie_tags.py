from django import template
from movies.models import Category, Genre, Movie

register = template.Library()


@register.simple_tag()
def get_category():
    return Category.objects.all()


@register.inclusion_tag('movies/tags/last_movies.html')
def get_last_movie():
    movies = Movie.objects.order_by('id')[:5]
    return {'last_movies': movies}


@register.simple_tag()
def get_genre():
    return Genre.objects.all()
