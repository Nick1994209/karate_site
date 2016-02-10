# -*-coding:utf8 -*-
import datetime

from django.shortcuts import render
from karate.models import PlanOfEvents, Articles


def additionally(request):

    return render(request, 'karate/additionally.html')