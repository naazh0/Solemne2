from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)$', views.detalle_noticia, name='detalle_noticia'),
]