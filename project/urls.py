# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import auth2.urls
import core.urls
import karate.urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(auth2.urls)),
    url(r'', include(karate.urls)),
    url(r'', include(core.urls)),
    url(r'^$', 'core.views.index', name='index'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^grppll/', include('grappelli.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
