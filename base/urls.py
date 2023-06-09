from django.urls import path, include

import base.views as views

urlpatterns = [
    path('sendmsg', views.sendmessage, name='sendmsg'),
    path('', views.index, name='index'),

]
