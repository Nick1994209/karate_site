# -*- coding:utf-8 -*-
import datetime

from django import forms

from karate.models import Articles, PhotoAlbum, PlanOfEvents


class ArticleCreate(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('name', 'short_text', 'text')


class PhotoAlbumCreate(forms.ModelForm):

    class Meta:
        model = PhotoAlbum
        fields = ('name',)


class PlanOfEventsCreteForm(forms.ModelForm):

    class Meta:
        model = PlanOfEvents
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(PlanOfEventsCreteForm, self).__init__(*args, **kwargs)
        self.fields['time'].widget = forms.TextInput(attrs={'type': 'time'})
        self.fields['date'].initial = datetime.date.today()
        self.fields['date'].widget = forms.TextInput(attrs={'type': 'date'})
