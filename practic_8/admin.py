from django.contrib import admin
from .models import Image

# Register your models here.

@admin.register(Image)
class AdminProduct(admin.ModelAdmin):
    pass