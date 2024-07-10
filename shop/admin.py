from django.contrib import admin
from .models import Category, Product, Image

# Register your models here.

@admin.register(Category, Product, Image)
class AdminProduct(admin.ModelAdmin):
    pass