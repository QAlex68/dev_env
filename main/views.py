from django.http import HttpResponse
from django.shortcuts import render



def index(request) -> HttpResponse:
    context: dict = {
        'tile': 'Home - Главная',
        'content': 'Магазин мебели - HOME'
    }
    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    context: dict = {
        'tile': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему мы такие клевые и самые лучшие.',
    }

    return render(request, 'main/about.html', context)
