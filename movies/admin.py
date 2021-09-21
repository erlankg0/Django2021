from django.contrib import admin
from movies.models import Actor, Category, RatingStar, Rating, Reviews, Movie, MovieShort, Genre

admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
admin.site.register(Movie)
admin.site.register(MovieShort)
admin.site.register(Genre)
