from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv
from typing import Optional
from pathlib import Path


def get_stations(stations_file_path: str) -> Optional[list]:
    if not Path(stations_file_path).exists():
        print(f'file "{stations_file_path}" does not exist.')
        return None

    with open(stations_file_path, newline='', encoding='UTF-8') as stations_file:
        reader = csv.DictReader(stations_file)
        stations = []

        for row in reader:
            stations.append(
                {
                    'Name': row['Name'],
                    'Street': row['Street'],
                    'District': row['District']
                }
            )

        return stations if stations else None


def index_view(request):
    return redirect(reverse('bus_stations'))


def bus_stations_view(request):
    stations_file_path = settings.BUS_STATION_CSV
    content = get_stations(stations_file_path)

    if not content:
        return HttpResponse(f'No stations found in the file "{stations_file_path}."')

    try:
        page_number = int(request.GET.get('page', 1))
    except ValueError:
        return HttpResponse(f'Parameter "page" must be an int!')
    else:
        paginator = Paginator(content, settings.ELEMENTS_PER_PAGE)
        page = paginator.get_page(page_number)
        stations = page.object_list

        context = {
            'bus_stations': stations,
            'page': page,
        }

    return render(request, 'stations/index.html', context)
