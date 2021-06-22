from django.urls import path
from apps.users.api.api import UserAPIVIew

urlpatterns = [
    path('usuarios/', UserAPIVIew.as_view(), name='usuarios'),
]