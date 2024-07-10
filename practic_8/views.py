from django.shortcuts import render
from .models import Image

# Create your views here.

def image(request):
    books = Image.objects.all()
    return render(request, 'image.html', context= {
        'books': books
    })
    

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'products.html')

def info_herself(request):
    return render(request, 'info_herself.html')