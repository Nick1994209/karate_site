# -*-coding:utf8 -*-
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.core.files.base import File
from django.core.urlresolvers import reverse

from django.shortcuts import render, redirect
from django.views.generic.detail import SingleObjectMixin
from core.models import User
from karate.models import Articles, Photo, PhotoAlbum, Videos
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from karate import forms


class LoginRequiredMixin(object): #TODO для более приятного добавления
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class PhotoAlbumListView(SingleObjectMixin, ListView):
    paginate_by = 10
    model = PhotoAlbum
    template_name = 'karate/multimedia/photo_album_list.html'
    queryset = PhotoAlbum.objects.order_by('-dc')

    def get(self, request, *args, **kwargs):
        self.object = self.get_queryset()
        return super(PhotoAlbumListView, self).get(request, *args, **kwargs)

photo_album_list_view = PhotoAlbumListView.as_view()


def photo_album_create(request):
    c = {}
    form = forms.PhotoAlbumCreate(request.POST or None)

    user = request.user
    if user.is_anonymous():
        return redirect(photo_album_list_view)

    if form.is_valid():
        print request.POST
        if form.cleaned_data['name']:
            photo_album = PhotoAlbum.objects.create(name=form.cleaned_data['name'])
        if request.FILES.get('files'):
            print request.FILES.get('files')
            image = request.FILES.get('files')
            photo_album.image=File(image)
            photo_album.save()
            return redirect(photo_album_list_view)
    c['form'] = form

    return render(request, 'karate/multimedia/photo_album_create.html', c)


class PhotoAlbumDelete(LoginRequiredMixin, DeleteView):
    model = PhotoAlbum
    template_name = 'karate/articles/article_delete.html'
    title = u'Удаление альбома'

    def get_success_url(self):
        return reverse(photo_album_list_view)

    def get_context_data(self, **kwargs):
        c = super(PhotoAlbumDelete, self).get_context_data(**kwargs)
        c['message'] = u'Вы действительно хотите удалить альбом "%s"' % self.get_object().name
        return c

photo_album_delete = PhotoAlbumDelete.as_view()


class PhotoListView(SingleObjectMixin, ListView):
    paginate_by = 30
    model = Photo
    template_name = 'karate/multimedia/photo_list.html'
    queryset = Photo.objects.all().order_by('-dc')

    def get_queryset(self):
        qs = super(PhotoListView, self).get_queryset()
        return qs.filter(photo_album__pk=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        # photo_album = PhotoAlbum.objects.get(pk=self.kwargs.get('pk'))
        self.object = self.get_queryset()
        return super(PhotoListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        c = super(PhotoListView, self).get_context_data(**kwargs)
        c['album_pk'] = self.kwargs.get('pk')
        return c

photo_list_view = PhotoListView.as_view()


def photo_add(request, pk):
    album_pk = int(pk)
    album = PhotoAlbum.objects.get(pk=album_pk)

    if request.POST:
        for file_ in request.FILES.getlist('files'):
            album.photos.create(image=File(file_), )
    succes_url = reverse(photo_list_view, kwargs={'pk': album_pk})
    return redirect(succes_url)


class PhotoDelete(LoginRequiredMixin, DeleteView):
    model = Articles
    template_name = 'karate/articles/article_delete.html'
    title = u'Удаление статьи'

    def get_success_url(self):
        return reverse(photo_list_view)

    def get_context_data(self, **kwargs):
        c = super(PhotoDelete, self).get_context_data(**kwargs)
        c['message'] = u'Вы действительно хотите удалить статью "%s"' % self.get_object().name
        return c

photo_delete = PhotoDelete.as_view()


class VideosListView(SingleObjectMixin, ListView):
    model = Videos
    queryset = Videos.objects.order_by('-dc')
    template_name = 'karate/multimedia/video_list.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_queryset()
        return super(VideosListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        c = super(VideosListView, self).get_context_data(**kwargs)
        c['title'] = 'videos'
        return c

video_list_view = VideosListView.as_view()


# class PeopleListView(SingleObjectMixin, ListView):
#     model = User
#     queryset = User.objects.all().exclude(is_staff=False)
#     template_name = 'karate/people_list.html'
#
#     def get(self, request, *args, **kwargs):
#         self.object = User.objects.order_by('-date_joined').exclude(is_staff=True)
#         return super(PeopleListView, self).get(request, *args, **kwargs)
#
# people_list_view = PeopleListView.as_view()
