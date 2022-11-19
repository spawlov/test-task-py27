# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from datetime import timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import Mailing
from .tasks import send_emails_to_subscribers


@receiver(post_save, sender=Mailing)
def test_task(sender, instance, created, *args, **kwargs):
    """По факту добавления новой рассылки - добавляем задание в Celery"""
    if created:
        send = instance.send
        # Если время отложенной отправки введено некорректно
        # (меньше текущего времени) - корректируем на текущее
        # +5 секунд на задержки обработки команды
        if send < timezone.now():
            send = timezone.now() + timedelta(seconds=5)
        send_emails_to_subscribers.apply_async((instance.id,), eta=send)
