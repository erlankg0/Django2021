"""
Модели¶
Модель является единственным источником информации о ваших данных. Она содержит основные поля и поведение данных,
которые вы храните. Как правило, каждая модель отображается в одну таблицу базы данных.

"""
from django.shortcuts import reverse
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')

    def get_absolute_url(self):
        return reverse('home', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Имя: {self.first_name}, Фамилия: {self.last_name}'


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tag_line = models.TextField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_ping_backs = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

    def __repr__(self):
        return self.headline
