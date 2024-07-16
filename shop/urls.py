from .views import logout_view, profile_view, base, home, products, info_herself, basket, get_product_detail, register_form, search_products, login_user
from django.urls import path

urlpatterns = [
    path('', base, name='base'),
    path('home', home, name='home'),
    path('products', products, name='products'),
    path('info_herself', info_herself, name='info_herself'),
    path('products/<int:pk>', get_product_detail, name='book_detail'),
    path('search', search_products, name='search'),
    path('register', register_form, name='register'),
    path('login', login_user, name='login'),
    path('profile', profile_view, name='profile'),
    path('logout', logout_view, name='logout'),
    
]