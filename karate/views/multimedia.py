# -*-coding:utf8 -*-
from django.core.files.base import File
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.views.generic import DeleteView, ListView

from core.views import LoginRequiredMixin
from karate import forms
from karate.models import Photo, PhotoAlbum, Videos


class PhotoAlbumListView(ListView):
    paginate_by = 10
    model = PhotoAlbum
    template_name = 'karate/multimedia/photo_album_list.html'
    queryset = PhotoAlbum.objects.order_by('-dc')


photo_album_list_view = PhotoAlbumListView.as_view()


def photo_album_create(request):
    user = request.user
    if user.is_anonymous():
        return redirect(photo_album_list_view)

    c = {}
    form = forms.PhotoAlbumCreate(request.POST or None)
    if form.is_valid() and request.FILES.get('files'):
        photo_album = PhotoAlbum.objects.create(name=form.cleaned_data['name'])
        photo_album.image = File(request.FILES['files'])
        photo_album.save()
        return redirect(photo_album_list_view)
    c['form'] = form
    c['message'] = 'Не были переданы файлы или форма не валидна'
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


class PhotoListView(ListView):
    paginate_by = 30
    model = Photo
    template_name = 'karate/multimedia/photo_list.html'
    queryset = Photo.objects.all().order_by('-dc')

    def get_queryset(self):
        qs = super(PhotoListView, self).get_queryset()
        return qs.filter(photo_album__pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        c = super(PhotoListView, self).get_context_data(**kwargs)
        c['album_pk'] = self.kwargs.get('pk')
        return c


photo_list_view = PhotoListView.as_view()


def photo_add(request, album_pk):
    album = PhotoAlbum.objects.get(pk=album_pk)

    if request.POST:
        for file_ in request.FILES.getlist('files'):
            album.photos.create(image=File(file_))
    success_url = reverse(photo_list_view, kwargs={'pk': album_pk})
    return redirect(success_url)


class PhotoDelete(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'karate/articles/article_delete.html'
    title = u'Удаление статьи'

    def get_success_url(self):
        return reverse(photo_list_view)

    def get_context_data(self, **kwargs):
        c = super(PhotoDelete, self).get_context_data(**kwargs)
        c['message'] = u'Вы действительно хотите удалить фото "%s"?' % self.get_object().title
        return c


photo_delete = PhotoDelete.as_view()


class VideosListView(ListView):
    model = Videos
    queryset = Videos.objects.order_by('-dc')
    template_name = 'karate/multimedia/video_list.html'

    def get_context_data(self, **kwargs):
        c = super(VideosListView, self).get_context_data(**kwargs)
        c['title'] = 'videos'
        return c


video_list_view = VideosListView.as_view()
