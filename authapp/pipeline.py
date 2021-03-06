from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden
from authapp.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    # print('response:', response)   # для отладки
    if backend.name != 'vk-oauth2':
        return

    if response.get('photo'):
        # print(f" PHOTO --> {response.get('photo')}")  # для отладки
        avatar_url = response.get('photo')
    elif response.get('user_photo'):
        # print(f" USER_PHOTO --> {response.get('user_photo')}")  # для отладки
        avatar_url = response.get('user_photo')
    else:
        avatar_url = None

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about')),
                                                access_token=response['access_token'], v='5.89')),
                          None
                          ))
    resp = requests.get(api_url)
    if resp.status_code != 200:
        return
    data = resp.json()['response'][0]
    # print(f'DATA --> {data}')
    if data.get('sex'):
        user.shopuserprofile.gender = ShopUserProfile.MALE if data.get('sex') == 2 else ShopUserProfile.FEMALE
    if data.get('about'):
        user.shopuserprofile.aboutMe = data.get('about')
    if data.get('bdate'):
        bdate = datetime.strptime(data.get('bdate'), '%d.%m.%Y').date()
        age = timezone.now().date().year - bdate.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')
        else:
            user.age = age
            user.save(avatar_url=avatar_url)

