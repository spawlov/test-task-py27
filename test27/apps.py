# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class Test27Config(AppConfig):
    name = 'test27'
    verbose_name = 'Сервис рассылки'

    def ready(self):
        from . import signals
