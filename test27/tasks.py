# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from string import Template

from django.conf import settings
from django.core import mail

from .models import Mailing, Subscriber


@shared_task
def send_emails_to_subscribers(mailing_id):
    """Задача для Celery - отправка писем подписчикам"""
    # Формируем список рассылки
    mailing_data = Mailing.objects.get(pk=mailing_id)
    mailing_list = list(
        Subscriber.objects.all().values_list(
            'email', 'firstname', 'lastname', 'birthday')
    )
    if len(mailing_list):
        # Подключаемся к SMTP серверу
        counter_mails = 0
        connection = None
        try:
            connection = mail.get_connection()
            connection.open()
        except Exception as e:
            print(e)
        else:
            # Подготовка писем и отправка за одно подключение
            for email, firstname, lastname, birthday in mailing_list:
                replace_dict = {
                    'email': email,
                    'firstname': firstname,
                    'lastname': lastname,
                    'birthday': birthday,
                }
                template_content = Template(mailing_data.letter)
                html_content = template_content.safe_substitute(**replace_dict)
                template_subject = Template(mailing_data.subject)
                letter_subject = template_subject.safe_substitute(
                    **replace_dict)
                message = mail.EmailMultiAlternatives(
                    subject=letter_subject,
                    from_email=settings.EMAIL,
                    to=[email],
                    connection=connection,
                )
                message.extra_headers = {
                    'X-Confirm-Reading-To': settings.EMAIL,
                    'Disposition-Notification-To': settings.EMAIL,
                }
                message.attach_alternative(html_content, 'text/html')
                message.send()
                counter_mails += 1
        finally:
            connection.close()
        return 'Sent ' + str(counter_mails) + ' Emails'
    else:
        return 'Mailing list is empty'
