# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager)
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True, verbose_name='Логин пользователя')
    email = models.EmailField(verbose_name='Email')

    f_name = models.CharField(max_length=100, verbose_name='Имя пользователя', blank=True)
    l_name = models.CharField(max_length=100, verbose_name='Фамилия', blank=True)
    avatar = models.ImageField(verbose_name='Аватар', upload_to='core/user/avatars/', blank=True)

    is_staff = models.BooleanField(default=False, verbose_name='Доступ в админ.панель')
    is_active = models.BooleanField(default=False, verbose_name='Доступ пользователя в систему')

    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    dm = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
