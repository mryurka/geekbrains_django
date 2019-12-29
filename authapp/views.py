from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from authapp.forms import ShopUserLoginForm
from authapp.forms import ShopUserRegisterForm
from authapp.forms import ShopUserEditForm
from django.contrib import auth
from django.urls import reverse

# Create your views here.


def login(request):

    title = 'вход'
    target_url = reverse('mainapp:main')

    if request.method == 'GET':
        target_url = request.META.get('HTTP_REFERER')
        if request.GET.get('next'):
            print(request.GET['next'])
            target_url = request.GET.get('next')

    login_form = ShopUserLoginForm(data=request.POST)

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        target_url = request.POST['url']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)  # Аутентификация считается успешной, если объект пользователя появился в request
            return HttpResponseRedirect(target_url)

    context = {'title': title, 'login_form': login_form, 'incoming_url': target_url}

    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:main'))


def register(request):
    title = 'регистрация'
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    context = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', context)


def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)
        content = {'title': title, 'edit_form': edit_form}
        return render(request, 'authapp/edit.html', content)

