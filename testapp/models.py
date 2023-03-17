""" Модели для приложения Test"""

from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Rubric(MPTTModel):
    """ Модель для MPTT"""
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """ Возвращает абсолютную ссылку"""
        return reverse('rubric', kwargs={"pk": self.pk})

    class MPTTMeta:
        """ Метакласс для MPTT"""
        order_insertion_by = ['name']


class Article(models.Model):
    """ Модель Article"""
    name = models.CharField(max_length=50)
    category = TreeForeignKey(Rubric, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
