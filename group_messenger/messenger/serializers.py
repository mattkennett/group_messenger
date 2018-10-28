# Imports from Django
from django.contrib.auth.models import User

# Imports from Django Rest Framework
from rest_framework import serializers

# Imports from messenger app
from messenger.models import Channel, Message



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', )

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('pk', 'name', )

class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('user', 'channel', 'timestamp', 'message',)
