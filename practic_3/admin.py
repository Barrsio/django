from django.contrib import admin
from .models import Author, Book


# Register your models here.

@admin.register(Author, Book)
class AdminProduct(admin.ModelAdmin):
    pass