# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Articles(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    dc = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания статьи')
    short_text = models.CharField(max_length=255, verbose_name='Краткое содержание')
    text = models.TextField(verbose_name='Текст статьи')

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'

    def __unicode__(self):
        return self.name


class PlanOfEvents(models.Model):
    date = models.DateField(verbose_name="Дата мероприятия")
    name = models.CharField(max_length=155, verbose_name='Название мероприятия')
    sity = models.CharField(max_length=100, verbose_name='Город')
    place = models.CharField(max_length=100, blank=True, verbose_name='Место провидения')
    time = models.TimeField(blank=True, verbose_name='Время начала')
    additionally = models.CharField(max_length=255, blank=True, verbose_name='Дополнительная информация')

#http://www.kyokushinkarate.ru/plan-meropriyatiy/
    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'Мероприятия'


class PhotoAlbum(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название альбома')
    image = models.ImageField(upload_to='photo_album/', blank=True, verbose_name='Фон альбома')
    dc = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Фото альбом'
        verbose_name_plural = 'Фото альбомы'

    def __unicode__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if self.photos:
            for photo in self.photos.all():
                photo.delete()
        storage, path = self.image.storage, self.image.path
        super(PhotoAlbum, self).delete(*args, **kwargs)
        storage.delete(path)


class Photo(models.Model):

    photo_album = models.ForeignKey(PhotoAlbum, related_name='photos')
    image = models.ImageField(verbose_name='Картинка', upload_to='album/photo/')
    title = models.CharField(max_length=255, blank=True, verbose_name='Описание')
    dc = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def save(self, *args, **kwargs):
        for field in self._meta.fields:
            if field.name == 'image':
                field.upload_to = 'album/%d/photos/' % self.photo_album_id
        super(Photo, self).save()

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.image.storage, self.image.path
        # Delete the model before the file
        super(Photo, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)

    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотографии'


class Videos(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name='Название')
    href = models.CharField(max_length=255, verbose_name='Урл')
    dc = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __unicode__(self):
        return self.name