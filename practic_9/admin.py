from django.contrib import admin
from .models import Image, Products

# Register your models here.

@admin.register(Image, Products)
class AdminProduct(admin.ModelAdmin):
    pass