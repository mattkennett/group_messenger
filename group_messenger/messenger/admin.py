# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Imports from Django
from django.contrib import admin

# Imports from messenger app
from messenger.models import *

admin.site.register(Channel)
admin.site.register(Message)