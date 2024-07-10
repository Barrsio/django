from .views import view_home, hello
from django.urls import path

urlpatterns = [
    path('home', view_home),
    path('hello', hello),
]