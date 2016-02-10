# -*- coding:utf-8 -*-
from PIL import Image
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.contrib import auth
from django.core.context_processors import csrf
# from core.forms import CreateGroupForm, GetGroupForm
import core
from core.models import User #, GroupUsers
from forms import LoginForm, RegistrationForm, FillingUserData
from django.core.files import File


def login(request):
    c = {}
    c.update(csrf(request)) #уточнить нужно ли
    form = LoginForm(request.POST or None)

    if request.user.username:
        return redirect('/')

    c['form_post'] = form

    if form.is_valid():
        print 'я валиден'
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        # email = form.cleaned_data['email']
        user = User.objects.all()

        authed = auth.authenticate(username=username, password=password)
        if authed is not None:
            auth.login(request, authed)
            from core import views
            succes_url = reverse(core.views.index)
            return redirect(succes_url) #TODO добавить редирект
        else:
            if not user.filter(username__iexact=username):
                c['login_error'] = "Пользователь не найден"
            # elif not user.filter(email=email):
            #     c['login_error'] = 'Неправильная почта'
            else:
                c['login_error'] = 'Неправильный пароль'
            return render(request, 'auth2/login.html', c)
    else:
        return render(request, 'auth2/login.html', c)


# def logout(request):
#     auth.logout(request)
#     return redirect("/auth2/auth2")

def register(request):
    c = {}
    c.update(csrf(request))
    form = RegistrationForm(request.POST or None)

    if request.user.username:
        return redirect('/')
    
    c['form_post'] = form
    if form.is_valid():
        user = form.save()
        authed = auth.authenticate(username=user.username, password=form.cleaned_data['password2'])
        if authed is not None:
            auth.login(request, authed)
            # return redirect('/map') #TODO добавить редирект
            return redirect(filling_user_data)

    return render(request, 'auth2/register.html', c)


def filling_user_data(request):
    c = {}

    if not request.user.username:
        return redirect(login)
    user = request.user
    form = FillingUserData(request.POST or None)

    print request.POST
    if form.is_valid():
        if form.cleaned_data['f_name']:
            user.f_name = form.cleaned_data['f_name']
        if form.cleaned_data['l_name']:
            user.l_name = form.cleaned_data['l_name']
        if request.FILES.get('files'):
            print request.FILES.get('files')
            image = request.FILES.get('files')
            user.avatar=File(image)

            #создание мини изображения, что бы быстрее грузиласть страница
            # mini_avatar= Image.new('RGBA', (32, 32), 'white') #задаем размер миниизображения
            # mini_avatar.paste(image, None, image)
            # if user.mini_avatar:
            #     mini_avatar.save(user.mini_avatar.path, quality=90)
            # else:
            #     user.avatar_mini=File(image, name=user.id)
            #     mini_avatar.save(user.mini_avatar.path, quality=90)
        user.save()
        return redirect(user_detail)

    c['form'] = form
    return render(request, 'auth2/filling_user_data.html', c)


def user_detail(request):
    if not request.user.username:
        return redirect(login)
    user = request.user
    # form = CreateGroupForm(request.GET or None)
    # if form.is_valid():
    #     if form.cleaned_data['name']:
    #         group_user = GroupUsers.objects.create(name=form.cleaned_data['name']) #без проверки, ибо проверка есть в самой форме
    #
    #     if form.cleaned_data['text']:
    #         group_user.text = form.cleaned_data['text']
    #         group_user.save()
    #     group_user.users.add(user)
    #     return redirect(user_detail) #иначе 100500 раз сохранит нашу группу

    c = {'user': user}# 'form': form}
    # if GroupUsers.objects.count() > 0:
    #     group_form = GetGroupForm(request.POST or None)
    #     if group_form.is_valid():
    #         print group_form.cleaned_data['group']
    #         if group_form.cleaned_data['group'] != None:
    #             user.group_users.add(group_form.cleaned_data['group'])
    #             user.save()
    #         return redirect(user_detail)
    #
    #     c['group_form'] = group_form

    return render(request, 'auth2/user_detail.html', c)