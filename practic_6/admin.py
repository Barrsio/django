from django.contrib import admin
from .models import Author, Publisher, Book

# Register your models here.

@admin.register(Author, Publisher, Book)
class AdminProduct(admin.ModelAdmin):
    pass