""" Контроллер приложения News"""

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView

from .forms import ContactForm, NewsForm, UserLoginForm, UserRegisterForm
from .models import Category, News


def contact(request):
    """ Контроллер для отправки E-mail"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'ilmen542@mail.ru',
                             ['ilmen542@mail.ru'], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка валидации')
    else:
        form = ContactForm()
    return render(request, 'news/contact.html', {"form": form})


def register(request):
    """ Регистрация пользователя"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрированы')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {"form": form})


def user_login(request):
    """ Регистрация пользователя"""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {"form": form})


def user_logout(request):
    """ Выход пользователя"""
    logout(request)
    return redirect('login')


class HomeNews(ListView):
    """ Класс для новостей"""
    model = News
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        """ Добавление дополнительных данных в контекст"""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        """ Фильтр"""
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    """ Класс для новостей по категориям"""
    model = News
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        """ Добавление дополнительных данных в контекст"""
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        """ Фильтр"""
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    """ Класс для просмотра одной новости"""
    model = News
    context_object_name = 'news_item'


class CreateNews(LoginRequiredMixin, CreateView):
    """ Класс создания объекта News"""
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'
