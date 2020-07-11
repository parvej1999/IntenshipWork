from django.urls import path, include
from django.contrib.auth import urls as auth_urls
from . import views

urlpatterns = [
    path('', include(auth_urls)),
    path('sign-up/', views.sign_up),
]
