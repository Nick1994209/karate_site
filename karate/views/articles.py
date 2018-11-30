# -*-coding:utf8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.views.generic.detail import SingleObjectMixin

from core.models import User
from karate import forms
from karate.models import Articles


class LoginRequiredMixin(object): #TODO для более приятного добавления
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class ArticleListView(SingleObjectMixin, ListView):
    #get_context_object_name
    paginate_by = 5
    model = Articles
    template_name = 'karate/articles/article_list.html'
    queryset = Articles.objects.order_by('-dc')

    def get(self, request, *args, **kwargs):
        # queryset = super(ArticleListView, self).get_queryset()
        self.object = super(ArticleListView, self).get_queryset()
        return super(ArticleListView, self).get(request, *args, **kwargs)

article_list_view = ArticleListView.as_view()


class ArticleDetailView(DetailView):

    queryset = Articles.objects.all()
    template_name = 'karate/articles/article_detail.html'

article_detail_view = ArticleDetailView.as_view()


class ArticlesCreate(LoginRequiredMixin, CreateView):#TODO добавить возможность откидываться назад
    model = Articles
    form_class = forms.ArticleCreate
    template_name = 'karate/articles/article_create.html'

    def get_success_url(self):
        return reverse(article_detail_view, kwargs={'pk': self.object.id})

article_create = ArticlesCreate.as_view()


class ArticlesUpdate(LoginRequiredMixin, UpdateView):
    model = Articles
    form_class = forms.ArticleCreate
    template_name = 'karate/articles/article_create.html'

    def get_success_url(self):
        return reverse(article_detail_view, kwargs={'pk': self.object.id})

article_update = ArticlesUpdate.as_view()


class ArticlesDelete(LoginRequiredMixin, DeleteView):
    model = Articles
    template_name = 'karate/articles/article_delete.html'
    title = u'Удаление статьи'

    def get_success_url(self):
        return reverse(article_list_view)

    def get_context_data(self, **kwargs):
        c = super(ArticlesDelete, self).get_context_data(**kwargs)
        c['message'] = u'Вы действительно хотите удалить статью "%s"' % self.get_object().name
        return c

article_delete = ArticlesDelete.as_view()
