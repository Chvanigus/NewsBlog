""" Контроллеры для тестового приложения"""
from django.shortcuts import render


def test(request):
    """Main"""
    return render(request, 'testapp/test.html')

