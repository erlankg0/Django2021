from django.db import models
from django.shortcuts import reverse
import datetime


class Category(models.Model):
    """ Модель категории
    # имя - Char
    # описание - Text
    # url - Slug
    """

    name = models.CharField(verbose_name='Категория', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=155)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.url})


class Actor(models.Model):
    """
        Актеры/Актрисы т режиссёры
    имя - Char
    возраст - Int
    описание - Text
    изображение - Image
    """

    name = models.CharField(verbose_name='Категория', max_length=150)
    age = models.PositiveSmallIntegerField('Возвраст', default=0)
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='actors/', verbose_name='Изображения')
    slug = models.SlugField(verbose_name='URL')

    class Meta:
        ordering = ['name']
        verbose_name = 'Актер/Актриса и режиссёр'
        verbose_name_plural = 'Актеры/Актрисы и режиссёры'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor', kwargs={'slug': self.slug})


class Genre(models.Model):
    """
            Жанры.
        имя - Char
        описание - Text
        url - Slug
    """

    name = models.CharField(verbose_name='Категория', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=155)

    class Meta:
        ordering = ['name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre', kwargs={'slug': self.url})


class Movie(models.Model):
    """Фильмы
        название - Char
        слоган - Char
        описание - Text
        постер - Image
        год - Date
        страна - Char
        режиссер - M2M
        актеры - M2M
        жанр - M2M
        премьера в мире - Data
        бюджет - Char
        сборы в США - Char
        сборы в мире - Char
        категория - FK
        url - Slug
        черновик - Bool
    """

    title = models.CharField(verbose_name="Название фильма", max_length=250)
    slogan = models.CharField(verbose_name='Слоган', max_length=250)
    description = models.TextField(verbose_name='Описания')
    poster = models.ImageField(upload_to='movie/', max_length=250)
    year = models.DateField(verbose_name='Год')
    country = models.CharField(verbose_name='Страна', max_length=200)
    directors = models.ManyToManyField(Actor, verbose_name='Режиссёр', related_name='film_direct')
    actors = models.ManyToManyField(Actor, verbose_name='Актеры', related_name='film_actor')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    world_premier = models.DateField(verbose_name='Премьера в мире', default=datetime.datetime.today)
    budget = models.PositiveIntegerField(verbose_name='Бюджет фильма.', default=0,
                                         help_text='Указываеть в долларах USA')
    fees_in_world = models.PositiveIntegerField(verbose_name='Сборы для фильма', default=0,
                                                help_text='Указываеть в долларах USA')
    category = models.ForeignKey(Category, verbose_name='Категория фильма', max_length=100, on_delete=models.SET_NULL,
                                 null=True)
    url = models.SlugField(verbose_name='Ссылка на фильм')
    is_publish = models.BooleanField(verbose_name='Публиковать или нет?')

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_movie', kwargs={'slug': self.url})


class MovieShort(models.Model):
    """
        Кадры из фильма
    название - Char
    описание - Text
    изображение - Image
    фильм - FK
    """
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='movie_short/', verbose_name='Изображения')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Кадры из фильма'
        verbose_name = 'Кадр из фильма'
        ordering = ['title']


class RatingStar(models.Model):
    """ Звезда рейтинга"""
    value = models.PositiveSmallIntegerField('Звезды')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
    """
    Рейтинг

    ip - IP
    звезда - FK
    фильм - FK
    """
    ip = models.CharField(verbose_name='IP адрес', max_length=20)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='Звезда')
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True, verbose_name='Фильм')

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name_plural = 'Рейтинги'
        verbose_name = 'Рейтинг'


class Reviews(models.Model):
    """
            Отзывы
    email - Email
    name - Char
    text - Text
    родитель (кому ответили)
    фильм -  FK
    """
    email = models.EmailField(verbose_name='Е-почта')
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщения', max_length=3000, help_text='Максимум 3000 символов')
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} : {self.movie}'

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'
