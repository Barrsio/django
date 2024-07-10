from django.contrib import admin
from .models import Student, Course, Teacher


# Register your models here.

@admin.register(Student, Course, Teacher)
class AdminProduct(admin.ModelAdmin):
    pass