from django.conf.urls import url

from .views import AddSubscriber, SuccessSubscribe, unsubscribe

app_name = 'test27'
urlpatterns = [
    url(r'^$', AddSubscriber.as_view(), name='add_subscriber'),
    url(r'^subscribed/$', SuccessSubscribe.as_view(), name='subscribed'),
    url(r'^unsubscribe/$', unsubscribe),
]
