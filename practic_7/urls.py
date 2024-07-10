from .views import home, products, info_herself, base
from django.urls import path

urlpatterns = [
    path('', base),
    path('home', home),
    path('products', products),
    path('info_herself', info_herself),
]