# -*- coding:utf-8 -*-

from django import forms
from django.contrib import auth
from django.forms import ModelForm
from django.forms.widgets import PasswordInput

from core.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин призывателя', max_length=30)
    password = forms.CharField(label='Пароль', widget=PasswordInput)

    def __init__(self, *args, **kwargs):
        self._user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        # метод возвращает пользователя если пользователь с username и password находится в системе
        self._user = auth.authenticate(
            username=self.cleaned_data['username'], password=self.cleaned_data['password'],
        )
        if not self._user:
            raise forms.ValidationError('Не найден пользователь или неправильный пароль')

    def get_user(self):
        if self._user is None:
            raise forms.ValidationError('Перед получением пользователя '
                                        'нужно пройти валидацию у формы')
        return self._user


class RegistrationForm(ModelForm):
    error_messages = {
        'duplicate_username': 'Такое имя пользователя уже занято.',
        'password_mismatch': 'Пароли не совпадают',
        'duplicate_email': 'Данная почта уже используется',
    }
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput,
                                help_text='Введите тот же пароль.')

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',
            )
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2 or not password1:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class FillingUserData(forms.ModelForm):
    # f_name = forms.CharField(max_length=100, label='Имя')
    # l_name = forms.CharField(max_length=100, label='Фамилия')
    class Meta:
        model = User
        fields = ['f_name', 'l_name']
