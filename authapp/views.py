from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from authapp.forms import ShopUserLoginForm
from authapp.forms import ShopUserRegisterForm
from authapp.forms import ShopUserEditForm
from django.contrib import auth
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from authapp.models import ShopUser
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
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Аутентификация считается успешной, если объект пользователя появился в request
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
            user = register_form.save()
            if send_verify_mail(user):
                print('сообщение подтверждения отправлено')
                # сделать страничку
            else:
                print('ошибка отправки сообщения')
            return render(request, 'authapp/emailed.html')
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


def send_verify_mail(user):
    verify_link = reverse('authapp:verify',
                          kwargs={'email': user.email,
                                  'activation_key': user.activation_key
                                  })
    title = f'Подтверждение учетной записи {user.username} '
    message = f'Для подтверждения учетной записи {user.username} на портале {settings.DOMAIN_NAME} \n' \
        f'перейдите по ссылке: {settings.DOMAIN_NAME}{verify_link} '
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        else:
            print(f'error activation user: {user} ')
        return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'error activation user : {e.args}')
        return HttpResponseRedirect(reverse('mainapp:main'))

