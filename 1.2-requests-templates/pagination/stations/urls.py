from django.urls import path

from .views import index_view, bus_stations_view

urlpatterns = [
    path('', index_view, name='index'),
    path('bus_stations/', bus_stations_view, name='bus_stations'),
]
