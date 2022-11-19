# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.shortcuts import get_object_or_404

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


def unsubscribe(request):
    user = get_object_or_404(Subscriber, email=request.GET.get('user_email'))
    user.delete()
    return HttpResponse(
        '<center><h4>Вы успешно отписались от рассылки</h4></center>'
    )
