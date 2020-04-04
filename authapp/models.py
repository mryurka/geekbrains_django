from django.db import models
from datetime import timedelta
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

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

    def __str__(self):
        return self.username

