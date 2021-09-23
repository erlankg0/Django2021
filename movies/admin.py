from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from movies.models import Actor, Category, RatingStar, Rating, Reviews, Movie, MovieShort, Genre


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описания', widget=CKEditorWidget())

    class Meta:
        model = Movie
        fields = '__all__'


admin.site.site_title = 'Erlan Abdraimov'
admin.site.site_header = 'Erlan Abdraimov'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url',)
    list_display_links = ('id', 'name', 'url',)
    search_fields = ('name',)


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    def image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="50" style="border-radius: 50px;">')

    form = MovieAdminForm
    image.short_description = 'poster'
    list_display = ('id', 'image', 'title', 'category', 'country', 'url', 'is_publish')
    list_display_links = ('id', 'image', 'title')
    list_editable = ('is_publish',)
    list_filter = ('category', 'year',)
    search_fields = ('title', 'description', 'category__name', 'genre__name',)
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    prepopulated_fields = {'url': ('title',)}


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'parent', 'movie')
    list_display_links = list_display
    readonly_fields = ('name', 'email',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50" style="border-radius: 50px;">')

    get_image.short_description = 'Изображения'

    list_display_links = ('id', 'name', 'age', 'get_image')
    list_display = ('id', 'name', 'age', 'get_image')
    fields = ('name', 'age', 'description', 'image', 'slug',)
    readonly_fields = ('get_image',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display_links = ('movie', 'ip', 'star')
    list_display = ('movie', 'ip', 'star')


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('value',)
    list_display_links = list_display


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display_links = ('name', 'url',)
    list_display = list_display_links


@admin.register(MovieShort)
class MovieShotAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie')
    list_display_links = list_display

# admin.site.register(Actor)
# admin.site.register(Rating)
# admin.site.register(RatingStar)
# admin.site.register(Reviews)
# admin.site.register(Movie)
# admin.site.register(MovieShort)
# admin.site.register(Genre)
