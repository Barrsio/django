from django.shortcuts import render

# Create your views here.

def get_book(request):
    return render(request, 'library.html',{
        'Name_book': 'Книга ',
        'Autor': 'Автор'
    })