# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import AuthenticationForm

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Field, Div, HTML, BaseInput, Button
# from crispy_forms.bootstrap import FormActions
# from core.models import GroupUsers


class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid': 'Неверный логин или пароль.',
        'invalid_login': 'Неверный логин или пароль.',
        'inactive': 'Ваш аккаунт заблокирован.'
    }

    username = forms.CharField(label='', max_length=80, required=True)
    password = forms.CharField(label='', widget=forms.PasswordInput(render_value=False), required=True)

    fname = forms.CharField(label=u'Фамилия', max_length=35, required=True)
    lname = forms.CharField(label=u'Имя', max_length=35, required=True)
    mname = forms.CharField(label=u'Отчество', max_length=35, required=True)
    email = forms.EmailField(label=u'Почта', required=True)

    #TODO я в шоке от того, что ниже происходит
    # def __init__(self, request=None, *args, **kwargs):
    #     super(LoginForm, self).__init__(request, *args, **kwargs)
    #     self.fields['username'].widget.attrs['placeholder'] = 'Номер телефона'
    #     self.fields['password'].widget.attrs['placeholder'] = 'Пароль'
    #     self.helper = FormHelper()
    #     self.helper.form_action = reverse_lazy('login')
    #     self.helper.form_method = 'post'
    #     self.helper.form_class = 'form-vertical login-form'
    #     self.helper.layout = Layout(
    #         HTML('<h3 class="form-title">Войти в аккаунт реестра</h3>'),
    #         Div(
    #             HTML('<i class="icon-phone"></i>'),
    #             Field('username', css_class='masked-phone'),
    #             css_class='input-icon'
    #         ),
    #         Div(
    #             HTML('<i class="icon-lock"></i>'),
    #             Field('password'),
    #             css_class='input-icon'
    #         ),
    #         FormActions(
    #             HTML("""
    #                 <a class="btn btn-default" href="{% url 'password_reset_enter_phone' %}">Вспомнить пароль</a>
    #                 <button type="submit" class="submit btn btn-primary pull-right">
    #                     Войти
    #                 </button>
    #             """)
    #         )
    #     )

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     from core.models import User
    #     user = User.objects.filter(username=username)
    #     if user:
    #         if user.is_active == False:
    #             return self.error_messages['inactive'] #или не так
    #         else:
    #             return username


# class CreateGroupForm(forms.ModelForm):
#     class Meta:
#         model = GroupUsers
#         fields = ['name', 'text']
#
#
# class GetGroupForm(forms.Form):
#     group = forms.ModelChoiceField(queryset=GroupUsers.objects.all(),
#                                    label='Название группы',to_field_name="name", initial=0, required=False)