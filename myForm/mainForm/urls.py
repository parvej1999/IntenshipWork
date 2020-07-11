# from django.conf.urls import patterns, include, url
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.displayForm, name='displayForm'),
]
