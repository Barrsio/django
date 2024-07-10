from .views import get_hello
from django.urls import path

urlpatterns = [
    path('', get_hello),
]