from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view_home(request):
    return HttpResponse('<h1> Привет</h1>')

def hello(request):
    return HttpResponse('<h1> Hello World!!!</h1>')

def book(request):
    return render(request, 'book.html', context={
        'title_book': 'Abababababab'
    })



