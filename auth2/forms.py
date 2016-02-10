# -*- coding:utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.forms.widgets import PasswordInput
from core.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label=u'Логин призывателя', max_length=30)
    password = forms.CharField(label=u'Пароль',widget=PasswordInput)


class RegistrationForm(ModelForm):
    error_messages = {
        'duplicate_username': (u"Такое имя пользователя уже занято."),
        'password_mismatch': (u"Пароли не совпадают"),
        'duplicata_email': (u'Данная почта уже используется'),
    }
    password1 = forms.CharField(label=u"Пароль",
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=u"Повторите пароль",
        widget=forms.PasswordInput,
        help_text=u"Введите тот же пароль, как указано выше, для проверки.")

    class Meta:
        model = User
        fields = ("username", 'email')

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicata_email'],
            code='duplicata_email',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user


class FillingUserData(forms.ModelForm):
    # f_name = forms.CharField(max_length=100, label='Имя')
    # l_name = forms.CharField(max_length=100, label='Фамилия')
    class Meta:
        model = User
        fields = ['f_name', 'l_name']
