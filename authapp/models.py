# import urllib
import os
from urllib.parse import urlparse
from urllib.request import urlretrieve
from datetime import timedelta
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


def get_exp():
    return now() + timedelta(hours=48)


class ShopUser(AbstractUser):

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    avatar = models.ImageField(upload_to='user_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='Возраст', default=18)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=get_exp())

    def is_activation_key_expired(self):
        return now() > self.activation_key_expires
        # if now() <= self.activation_key_expires:
        #     return False
        # else:
        #     return True

    def save(self, *args, **kwargs):
        # print(f'kwargs --> {kwargs}')  # для отладки
        if kwargs and kwargs.get('avatar_url'):
            avatar_url = kwargs['avatar_url']
            file_save_dir = os.path.join(settings.MEDIA_ROOT, 'user_avatars')
            filename = (urlparse(avatar_url).path.split('/')[-1]).split('?')[0]
            # print(f'filename --> {filename}')  # для отладки
            res = urlretrieve(avatar_url, os.path.join(file_save_dir, filename))
            # print('URLRETRIEVE -->', res)   # для отладки
            self.avatar = os.path.join(file_save_dir, filename)
        super().save()

    def __str__(self):
        return self.username


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )
    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='теги', max_length=128, blank=True)
    aboutMe = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)
        else:
            instance.shopuserprofile.save()

    # @receiver(post_save, sender=ShopUser)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.shopuserprofile.save()


