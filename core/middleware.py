# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import logging

import datetime

from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect


logging = logging.getLogger('request_log') #TODO для чего ?)


class LoginMiddleware(object):

    def process_request(self, request):
        # except_urls = settings.EXCEPT_URLS
        is_authenticated = request.user.is_authenticated()

        if not is_authenticated: # and not request.path.startswith(except_urls):
            # if request.path.startswith('/api/'):
            #     return HttpResponse('Unauthorized', status='401')
            # else:
            #     return redirect('/login/?next=%s' % request.get_full_path())
            pass
            # return redirect('/auth/') #TODO добавить переход


class AddDmUserMiddleware(object):

    def process_request(self, request):
        if request.user.is_authenticated():
            is_authenticated = request.user.is_authenticated()
            user = request.user
            request.user.save()


class RedirectMiddleware(object):

    def process_request(self, request):
        if not request.user.is_authenticated():
            list_forbiden_url = ['/map', ]
            for url in list_forbiden_url:
                if url in request.path:
                    return redirect('login')


class RedirectMapMiddleware(object):
    ''' запрещает не тому юзеру смотреть в чужие карты '''
    def process_request(self, request):
        if request.user.is_authenticated() and '/map/edit/' in request.path and not request.is_ajax():

            url = bytearray(str(request.path))
            # url.pop('/map/edit/')
            del url[:10]
            url = str(url)
            if '/' in url:
                id = ''
                for number in url:
                    if number == '/':
                        break
                    id += number
                id = int(id)
            else:
                if url != '':
                    id = int(url)
                else:
                    return redirect('map_list_view')

            if not request.user.maps.filter(id=id):
                return redirect('map_list_view')