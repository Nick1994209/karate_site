from django.conf.urls import patterns, url

urlpatterns = patterns('karate.views',
    url(r'^articles/$', 'articles.article_list_view', name='article_list'),
    url(r'^articles/(?P<pk>[0-9]+)/$', 'articles.article_detail_view', name='article-detail'),
    url(r'^articles/(?P<pk>[0-9]+)/delete/$', 'articles.article_delete', name='article_delete'),

    url(r'^articles/create/$', 'articles.article_create', name='article_create'),
    url(r'^articles/(?P<pk>[0-9]+)/update/$', 'articles.article_update', name='article_update'),
    url(r'^articles/create/$', 'articles.article_create', name='article_create'),

    url(r'^multimedia/photo_album/$', 'multimedia.photo_album_list_view', name='photo_album_list'),
    url(r'^multimedia/photo_album/create/$', 'multimedia.photo_album_create', name='photo_album_create'),
    url(r'^multimedia/photo_album/(?P<pk>[0-9]+)/delete/$', 'multimedia.photo_album_delete', name='photo_album_delete'),

    url(r'^multimedia/photo_album/(?P<pk>[0-9]+)/$', 'multimedia.photo_list_view', name='photo_list'),
    url(r'^multimedia/photo_album/(?P<pk>[0-9]+)/add/$', 'multimedia.photo_add', name='photo_add'),

    url(r'^multimedia/videos/$', 'multimedia.video_list_view', name='videos'),


    url(r'^events/$', 'plan_of_events.plan_of_events_list_view', name='plan_of_events_list'),
    url(r'^events/create/$', 'plan_of_events.plan_of_events_create', name='plan_of_events_create'),
    url(r'^events/(?P<pk>[0-9]+)/$', 'plan_of_events.plan_of_events_update', name='plan_of_events_update'),
    url(r'^events/(?P<pk>[0-9]+)/delete/$', 'plan_of_events.plan_of_events_delete', name='plan_of_events_delete'),

    url(r'^additionly/$', 'other.additionally', name='additionally'),
    )
