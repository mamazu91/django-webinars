from django.http import HttpResponse
from django.shortcuts import reverse, render
from datetime import datetime
from pathlib import Path


def curr_time_view(request):
    return HttpResponse(f'Текущее время: <br> {datetime.now().strftime("%H:%M:%S")}')


def workdir_view(request):
    path = Path('.')
    curr_work_dir_content = [item.name for item in path.iterdir()]
    return HttpResponse(
        f'Current working dir: <br> {path.cwd()} <br><br> Content: <br> {"<br>".join(curr_work_dir_content)}')


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }

    return render(request, template_name, context)
