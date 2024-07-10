from .views import get_book

from django.urls import path

urlpatterns = [
    path('library', get_book),
]