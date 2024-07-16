from django.contrib import admin
from .models import Category, Product, Image, Profile

# Register your models here.

@admin.register(Category, Product, Image, Profile)
class AdminProduct(admin.ModelAdmin):
    pass