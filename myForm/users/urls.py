from django.urls import path, include
from django.contrib.auth import urls as auth_urls
from . import views

urlpatterns = [
    path('accounts/', include(auth_urls)),
    path('', views.sign_up, name='signup'),
]
