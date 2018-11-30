from django.conf.urls import include, patterns, url

urlpatterns = patterns('core.views',
    url(r'^index/$', 'index', name='index'),
)
