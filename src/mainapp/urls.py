from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('create/', add, name='news_create_url'),
]
