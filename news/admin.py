from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import Category, News


class NewsAdminForm(forms.ModelForm):
    """ Форма для редактирования текста с загрузкой файлов"""
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    """ Класс настройки представления в Админке"""
    form = NewsAdminForm
    # Какие данные отображаются в модели News
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    # Какие данные являются ссылкой на редактирование записи
    list_display_links = ('id', 'title')
    # По каким столбцам производится поиск
    search_fields = ('title', 'content')
    # Редактируемые поля
    list_editable = ('is_published', )
    # Фильтрация по полям
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    """ Класс настройки представления в Админке"""
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


# Регистрация приложения и настройки в админке
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
