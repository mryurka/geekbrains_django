from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ShopUser(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    avatar = models.ImageField(upload_to='user_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='Возраст')

    def __str__(self):
        return self.username

