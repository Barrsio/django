from .views import view_home, hello, book
from django.urls import path

urlpatterns = [
    path('home', view_home),
    path('hello', hello),
    path('', book),
]