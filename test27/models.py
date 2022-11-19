# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


class Subscriber(models.Model):
    """Список подписчиков"""
    email = models.EmailField(verbose_name='Email', unique=True)
    firstname = models.CharField(max_length=64, verbose_name='Имя')
    lastname = models.CharField(max_length=64, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')

    # def get_absolute_url(self):
    #     return reverse('test27:subscribed')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'


class Mailing(models.Model):
    """Список рассылок"""
    name = models.CharField(max_length=128, verbose_name='Название рассылки')
    subject = models.CharField(max_length=128, verbose_name='Тема письма')
    letter = models.TextField(verbose_name='Шаблон письма')
    send = models.DateTimeField(verbose_name='Дата и время отправки')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создана')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
