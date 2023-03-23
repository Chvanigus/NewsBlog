""" Контроллеры для тестового приложения"""
from django.shortcuts import render

from .models import Rubric


def test(request):
    """Main"""
    return render(request, 'testapp/test.html', {'rubrics': Rubric.objects.all()})


def get_rubric(request):
    """ Получение рубрики"""
    pass
