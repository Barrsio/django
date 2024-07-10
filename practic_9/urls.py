from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from .views import home, products, info_herself, base, image, get_book_detail



urlpatterns = [
    path('', base, name='base'),
    path('home', home, name='home'),
    path('products', products, name='products'),
    path('info_herself', info_herself, name='info_herself'),
    path('image', image, name='image'),
    path('book/<int:pk>', get_book_detail, name='book_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)