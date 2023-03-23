""" Настройка админки"""

from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Article, Rubric

admin.site.register(
        Rubric,
        DraggableMPTTAdmin,
        list_display=(
            'tree_actions',
            'indented_title',
        ),
        list_display_links=(
            'indented_title',
        ),
)
admin.site.register(Article)
