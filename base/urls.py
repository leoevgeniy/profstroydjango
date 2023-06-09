from django.urls import path, include, re_path
from django.views.generic import RedirectView

import base.views as views

favicon_view = RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)

urlpatterns = [
    path('sendmsg', views.sendmessage, name='sendmsg'),
    path('', views.index, name='index'),
    re_path(r'^favicon\.ico$', favicon_view),

]
