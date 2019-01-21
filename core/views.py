import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from karate.models import Articles, PlanOfEvents


def index(request):
    c = {}
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    events = PlanOfEvents.objects.order_by('date').filter(date__gte=yesterday)
    if events:
        c['events'] = events[0]

    last_article = Articles.objects.order_by('-dc')
    if last_article:
        c['last_article'] = last_article[0]

    return render(request, 'core/index.html', c)


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view)
