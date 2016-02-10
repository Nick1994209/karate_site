# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('auth2.views',
    url(r'^login/$', 'login', name='login'),# пока так потом поправлю
    # url(r'^logout/$', 'logout', name='logout'),
    url(r'^register/$', 'register', name='register'),
    url(r'^filling_user_data/$', 'filling_user_data', name='filling_user_data'),
    url(r'^user_detail/$', 'user_detail', name='user_detail')
)