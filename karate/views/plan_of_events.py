# -*-coding:utf8 -*-
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.views.generic.detail import SingleObjectMixin

from core.models import User
from core.views import LoginRequiredMixin
from karate import forms
from karate.models import Articles, Photo, PhotoAlbum, PlanOfEvents


class PlanOfEventsListView(ListView):
    paginate_by = 10
    model = PlanOfEvents
    template_name = 'karate/plan_of_events/plan_of_events_list.html'
    queryset = PlanOfEvents.objects.order_by('-date')


plan_of_events_list_view = PlanOfEventsListView.as_view()


class PlanOfEventsView(LoginRequiredMixin):
    model = PlanOfEvents
    form_class = forms.PlanOfEventsCreteForm
    template_name = 'karate/plan_of_events/plan_create.html'

    def get_success_url(self):
        return reverse(plan_of_events_list_view)

    def get_context_data(self, **kwargs):
        c = super(PlanOfEventsView, self).get_context_data()
        c['form_post'] = self.form_class
        return c


class PlanOfEventsCreateView(PlanOfEventsView, ListView):
    pass


plan_of_events_create = PlanOfEventsCreateView.as_view()


class PlanOfEventsUpdateView(PlanOfEventsView, UpdateView):
    def get_context_data(self, **kwargs):
        c = super(PlanOfEventsUpdateView, self).get_context_data()
        c['object'] = PlanOfEvents.objects.get(pk=self.kwargs['pk'])
        c['edited'] = True
        return c


plan_of_events_update = PlanOfEventsUpdateView.as_view()


class PlanOfEventsDeleteView(LoginRequiredMixin, DeleteView):
    model = PlanOfEvents
    template_name = 'karate/articles/article_delete.html'

    def get_success_url(self):
        return reverse(plan_of_events_list_view)


plan_of_events_delete = PlanOfEventsDeleteView.as_view()
