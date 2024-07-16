from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from .models import Product, Profile
from .forms import RegisterForm, LoginForm
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth import logout


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

def basket(request):
    return render(request, 'basket.html')

def get_product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'detail_product.html', context={
        'product': product
    })
      
def register_form(request:HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = RegisterForm()   
    return render(request, 'register.html', context={
        'form':form
    })

def search_products(request):
    if request.method == "GET":
        search = request.GET['search']
        products = Product.objects.filter(
            Q(name__icontains = search) | Q(category__name__icontains = search))
        print(products)
        print(search)
        return render(request, template_name='found_product.html', context={
        'Products' : products,
        'title' : 'Товары'
        })
    return redirect(reverse('home'))

def login_user(request: HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', context={
        'title': 'Авторизация',
        'form': form
        })

@login_required(login_url='login')
def profile_view(request: HttpRequest):
    print(request.user)
    user = Profile.objects.select_related('user').get(user=request.user)
    
    return render(request, 'profile.html', context={
        'user' : user
    })
    


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))