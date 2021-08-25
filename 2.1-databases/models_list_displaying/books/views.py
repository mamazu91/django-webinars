from django.shortcuts import render, redirect
from books.models import Book
from django.core.paginator import Paginator
from django.conf import settings


def home_view(request):
    return redirect('catalog')


def catalog_view(request):
    books = Book.objects.all()
    template = 'books/catalog.html'
    context = {
        'books': books
    }
    return render(request, template, context)


def filtered_books_view(request, pub_date):
    books = Book.objects.filter(pub_date__year=pub_date[:4], pub_date__month=pub_date[5:7])

    page_number = int(request.GET.get('page', settings.ELEMENTS_PER_PAGE))
    paginator = Paginator(books, 1)
    page = paginator.get_page(page_number)
    books_per_page = page.object_list

    template = 'books/filtered_books.html'
    context = {
        'books': books_per_page,
        'pub_date': books_per_page[0].pub_date,
        'page': page
    }
    return render(request, template, context)
