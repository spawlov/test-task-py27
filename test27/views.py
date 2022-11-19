# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView

from .form import AddSubscriberForm
from .models import Subscriber


class AddSubscriber(CreateView):
    """Добавление подписчика"""
    model = Subscriber
    form_class = AddSubscriberForm
    template_name = 'add_subscriber.html'
    success_url = reverse_lazy('test27:subscribed')


class SuccessSubscribe(ListView):
    """Подписчик добавлен"""
    model = Subscriber
    template_name = 'success_subscribe.html'
