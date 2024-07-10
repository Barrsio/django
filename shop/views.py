from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def view_home(request):
    return HttpResponse('<h1> Привет</h1>')

def hello(request):
    return HttpResponse('<h1> Hello World!!!</h1>')

def base(request):
    return render(request, 'base.html')

def home(request):
    
    return render(request, 'home.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', context= {
        'Products': products,    
    })

def info_herself(request):
    return render(request, 'info_herself.html')



