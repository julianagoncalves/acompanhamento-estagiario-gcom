from django.conf.urls import patterns, include, url
from django.contrib import admin

from projeto_estagiario import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
