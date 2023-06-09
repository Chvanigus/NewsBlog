""" Формы заполнения модели News"""
import re

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import News


class ContactForm(forms.Form):
    """ Форма для электронной почты"""
    subject = forms.CharField(label='Тема письма',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст',
                              widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))


class UserLoginForm(AuthenticationForm):
    """ Форма авторизации пользователя"""
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    """ Форма регистрации пользователя"""
    username = forms.CharField(label='Имя пользователя',
                               help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewsForm(forms.ModelForm):
    """ Форма заполнения модели новости"""

    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        """ Кастомный валидатор"""
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название новости не должно начинаться с цифры')
        return title
