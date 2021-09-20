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
