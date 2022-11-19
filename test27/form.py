# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Subscriber


class AddSubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ['email', 'firstname', 'lastname', 'birthday']
