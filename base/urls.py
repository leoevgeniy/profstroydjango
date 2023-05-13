from django.contrib import admin
from django.urls import path, include

import base.views

urlpatterns = [
    path('', base.views.index, name='index'),
]
