# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Subscriber, Mailing


class Subscribers(admin.ModelAdmin):
    model = Subscriber
    list_display = ('email', 'firstname', 'lastname', 'birthday',)
    readonly_fields = ('created',)


class Mailings(admin.ModelAdmin):
    model = Mailing
    list_display = ('name', 'subject', 'created', 'send',)
    readonly_fields = ('created',)


admin.site.register(Subscriber, Subscribers)
admin.site.register(Mailing, Mailings)
