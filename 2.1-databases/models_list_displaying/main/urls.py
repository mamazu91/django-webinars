"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, register_converter

from books.views import home_view, filtered_books_view, catalog_view
from books.converters import PubDateConverter

register_converter(PubDateConverter, 'pdc')

urlpatterns = [
    path('', home_view, name='home'),
    path('books/<pdc:pub_date>/', filtered_books_view, name='filtered_books'),
    path('books/', catalog_view, name='catalog'),
    path('admin/', admin.site.urls),
]
