# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Imports from Django
from django.http import HttpResponse

# Imports from Django Rest Framework
from rest_framework import viewsets, permissions, generics

# Imports from messenger app
from messenger.models import Channel, Message
from messenger.serializers import ChannelSerializer, MessageSerializer

class ChannelViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class MessageViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Message.objects.all().order_by('-timestamp')
    serializer_class = MessageSerializer

    def create(self, request):
        channel_pk = request.POST['channel']
        message = request.POST['message']

        channel_object = Channel.objects.get(pk=channel_pk)

        newMessage = Message(
            user=request.user,
            channel=channel_object,
            message=message,
        )
        newMessage.save()

        return HttpResponse(status=201)

class ChannelMessagesView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = MessageSerializer

    def get_queryset(self):
        channel_pk = self.kwargs['channel']
        channel = Channel.objects.get(pk=channel_pk)
        return Message.objects.filter(channel=channel).order_by('-timestamp')[:25]
