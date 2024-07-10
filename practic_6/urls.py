from .views import get_book
from django.urls import path

urlpatterns = [
    path('', get_book),
]