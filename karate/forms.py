# -*- coding:utf-8 -*-
import datetime

from django import forms
from django.forms.extras import SelectDateWidget
from django.forms.widgets import SplitDateTimeWidget
from karate.models import Articles, PhotoAlbum, PlanOfEvents


class ArticleCreate(forms.ModelForm):
#widget=forms.Textarea

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
        self.fields['time'].widget = forms.TextInput(
                                        attrs={'type': 'time'},
                                        )
        self.fields['date'].initial = datetime.date.today()
        self.fields['date'].widget = forms.TextInput(
                                attrs={'type': 'date'}
                                )
        #
        # objects_ = PlanOfEvents.objects.filter(pk=self._meta.model.pk)
        # if object:
        #     a = 1
