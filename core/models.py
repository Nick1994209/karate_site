# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, UserManager


class User(AbstractBaseUser, PermissionsMixin):
    VERBOSE_NAME = 'Пользователь'

    username = models.CharField(max_length=100, unique=True, verbose_name='Логин пользователя')
    email = models.EmailField(verbose_name='Email')

    f_name = models.CharField(max_length=100, verbose_name='Имя пользователя', blank=True)
    l_name = models.CharField(max_length=100, verbose_name='Фамилия', blank=True)
    avatar = models.ImageField(verbose_name='Аватар', upload_to='core/user/avatars/', blank=True)

    is_staff = models.BooleanField(default=False, verbose_name='Доступ в админ.панель')
    is_active = models.BooleanField(default=False, verbose_name='Доступ пользователя в систему') #TODO уточнить, почему FALSE

    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации') #сранное поле, из-за него не мог создать пользователя
    dm = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    # rating = models.PositiveSmallIntegerField(default=0, verbose_name='Рейтинг')

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

#
# class GroupUsers(models.Model):
#     name = models.CharField(max_length=100, unique=True, verbose_name='Название')
#     text = models.TextField(verbose_name='Описание')
#     users = models.ManyToManyField(User, blank=True, related_name='group_users')
#     dc = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
#     # password = models.CharField(label='Пароль', blank=True, max_length=128)
#
#     def __unicode__(self):
#         return self.name
#     # user_create_group = models.ForeignKey(User, blank=True, verbose_name='Пользователь, создавший группу') TODO