from django.urls import path
from apps.users.api.api import user_api_view, user_detail_api_view

urlpatterns = [
    path('usuarios/', user_api_view, name='usuarios'),
    path('usuarios/<int:pk>/', user_detail_api_view, name='usuarios_detail_api_view'),
]