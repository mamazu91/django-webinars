from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', None)
    sort_mapping = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }

    if sort in sort_mapping:
        phones = Phone.objects.all().order_by(sort_mapping[sort])
    else:
        phones = Phone.objects.all()

    template = 'catalog.html'
    context = {
        'phones': phones
    }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }

    return render(request, template, context)
