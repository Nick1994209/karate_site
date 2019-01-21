# -*-coding:utf8 -*-
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from core.models import User
from core.views import LoginRequiredMixin
from karate import forms
from karate.models import Articles


def lists_articles(request):
    queryset = Articles.objects.order_by('-dc')
    paginator = Paginator(object_list=queryset, per_page=5)
    page = int(request.GET.get('page', 1))

    return render(request, template_name='karate/articles/article_list.html', context={
        'user': request.user,
        'page_obj': paginator.page(page),
    })


class ArticleListView(ListView):
    paginate_by = 5
    model = Articles
    template_name = 'karate/articles/article_list.html'
    queryset = Articles.objects.order_by('-dc')


article_list_view = ArticleListView.as_view()


class ArticleDetailView(DetailView):
    queryset = Articles.objects.all()
    template_name = 'karate/articles/article_detail.html'


article_detail_view = ArticleDetailView.as_view()


class ArticlesCreate(LoginRequiredMixin, CreateView):
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
