from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def index(request) -> HttpResponse:
    context: dict = {
        'tile': 'Home',
        'content': 'Главная страница магазина - HOME',
        'list': ['First', 'second'],
        'dict': {'first': 1},
        'bool': True,
        'is_authenticated': False,
    }

    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    return HttpResponse('About page')
