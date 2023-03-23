""" Кастомные теги для приложения News"""

from django import template
from django.db.models import F
from django.db.models.aggregates import Count

from news.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    """ Возвращает категории"""
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    """ Усложнённый тег, который рендерит данные по категориям новостей"""
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    return {"categories": categories}
