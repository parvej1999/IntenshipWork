# from django.conf.urls import patterns, include, url
from django.urls import include, path
from . import views

urlpatterns = [
    path('report-form/', views.displayForm, name='displayForm'),
    path('incident-list/', views.incidentList, name='incidentList'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
