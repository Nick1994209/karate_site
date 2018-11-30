# -*- coding:utf-8 -*-

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin

import auth2.urls
import core.urls
import karate.urls

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(auth2.urls)),
    url(r'', include(karate.urls)),
    url(r'', include(core.urls)),
    url(r'^$', 'core.views.index', name='index'),
    url(r'^grppll/', include('grappelli.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
