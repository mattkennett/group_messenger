# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Imports from Django
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Channel(models.Model):
    name = models.CharField(max_length=100)

class Message(models.Model):
    user = models.ForeignKey(User)
    channel = models.ForeignKey(Channel)
    timestamp = models.DateTimeField(default=timezone.now)
    message = models.TextField(max_length=512)