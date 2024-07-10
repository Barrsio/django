from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category, Product)
class AdminProduct(admin.ModelAdmin):
    pass