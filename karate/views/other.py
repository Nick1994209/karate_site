# -*-coding:utf8 -*-
import datetime

from django.shortcuts import render


def additionally(request):
    return render(request, 'karate/additionally.html')
