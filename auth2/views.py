from django.contrib import auth
from django.core.files import File
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render

import core
from core import views

from .forms import FillingUserData, LoginForm, RegistrationForm


def login(request):
    # если пользователь авторихован, то ему не нужно заного заходить
    if request.user.is_authenticated():
        return redirect('/')

    form = LoginForm(request.POST or None)
    c = {'form_post': form}

    if form.is_valid():
        auth.login(request, form.get_user())
        return redirect(reverse(core.views.index))
    return render(request, 'auth2/login.html', c)


def logout(request):
    auth.logout(request)
    return redirect("/auth2/auth2")


def register(request):
    if request.user.is_authenticated():
        return redirect('/')

    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        auth.login(request, user)
        return redirect(filling_user_data)

    return render(request, 'auth2/register.html', {'form_post': form})


def filling_user_data(request):
    if request.user.is_anonymous():
        return redirect(login)

    user = request.user
    form = FillingUserData(request.POST or None)

    if form.is_valid():
        if form.cleaned_data['f_name']:
            user.f_name = form.cleaned_data['f_name']
        if form.cleaned_data['l_name']:
            user.l_name = form.cleaned_data['l_name']
        if request.FILES.get('files'):
            image = request.FILES.get('files')
            user.avatar = File(image)

            # создание мини изображения, что бы быстрее грузиласть страница
            # mini_avatar= Image.new('RGBA', (32, 32), 'white') #задаем размер миниизображения
            # mini_avatar.paste(image, None, image)
            # if user.mini_avatar:
            #     mini_avatar.save(user.mini_avatar.path, quality=90)
            # else:
            #     user.avatar_mini=File(image, name=user.id)
            #     mini_avatar.save(user.mini_avatar.path, quality=90)
        user.save()
        return redirect(user_detail)

    return render(request, 'auth2/filling_user_data.html', {'form': form})


def user_detail(request):
    if request.user.is_anonymous():
        return redirect(login)

    return render(request, 'auth2/user_detail.html', {'user': request.user})
