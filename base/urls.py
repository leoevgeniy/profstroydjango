from django.contrib import admin
from django.urls import path, include

import base.views

urlpatterns = [
    path('', base.views.index, name='index'),
    path('sendmsg', base.views.sendmessage, name='sendmsg'),
]
