from django.shortcuts import render
from .models import Book, Publisher

# Create your views here.

def get_book(request):
    # name_info = Book.objects.get(id=1)
    publisher_name = Book.objects.exclude(name_publisher__name = "Васильевка")
    all_publisher = Publisher.objects.all()
    return render(request, 'books.html', context= {
        'Name_book': publisher_name,
        # 'Author': name_info,
        'Publisher': all_publisher,
        # 'Year': name_info
    })