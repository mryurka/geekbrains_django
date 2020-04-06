from django.core.management.base import BaseCommand
from authapp.models import ShopUser
from authapp.models import ShopUserProfile


class Command (BaseCommand):
    def handle(self, *args, **options):
        users = ShopUser.objects.filter(shopuserprofile__isnull=True)
        for user in users:
            print(user.name)
            users_profile = ShopUserProfile.objects.create(user=user)
            users_profile.save()


