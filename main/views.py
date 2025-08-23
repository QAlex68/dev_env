from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories



def index(request) -> HttpResponse:

    categories = Categories.objects.all()

    context: dict = {
        'tile': 'Home - Главная',
        'content': 'Магазин мебели - HOME',
        'categories': categories
    }
    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    context: dict = {
        'tile': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему мы такие клевые и самые лучшие.',
    }

    return render(request, 'main/about.html', context)
