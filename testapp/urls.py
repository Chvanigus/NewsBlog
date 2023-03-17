""" Маршруты для приложения testapp"""
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', test, name='test'),
]
