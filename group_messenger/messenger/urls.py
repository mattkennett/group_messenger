# Imports from Django
from django.conf.urls import url

from . import views

app_name = 'messenger'
urlpatterns = [
    url(r'^api/v1/channel-messages/(?P<channel>[0-9]+)', views.ChannelMessagesView.as_view()),
]
