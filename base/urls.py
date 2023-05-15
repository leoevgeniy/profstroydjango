from django.urls import path, include

import base.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('sendmsg', views.sendmessage, name='sendmsg'),
]
