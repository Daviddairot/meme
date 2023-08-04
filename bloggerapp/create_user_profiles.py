from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from .models import UserProfile

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            try:
                UserProfile.objects.get(user=user)
            except UserProfile.DoesNotExist:
                UserProfile.objects.create(user=user)