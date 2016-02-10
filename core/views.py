
# -*-coding:utf8 -*-
import datetime

from django.shortcuts import render
from karate.models import PlanOfEvents, Articles


def index(request):
    c = {}
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    events = PlanOfEvents.objects.filter(date__gte=yesterday).order_by('date')
    if events:
        c['events'] = events[0]

    last_article = Articles.objects.order_by('-dc')
    if last_article:
        c['last_article'] = last_article[0]

    return render(request, 'core/index.html', c)
