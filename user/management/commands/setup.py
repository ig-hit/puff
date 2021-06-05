import os

from django.contrib.auth import models, hashers
from django.core import management

from user import models as user_models


class Command(management.BaseCommand):
    def handle(self, *args, **kwargs):
        self._create_superuser()
        self._create_appuser()

    def _create_superuser(self):
        username = os.environ.get('INITIAL_SUPERUSER_USERNAME')
        password = os.environ.get('INITIAL_SUPERUSER_PASSWORD')

        try:
            models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            models.User.objects.create_superuser(
                username=username,
                password=password,
            )
            print(f'Superuser "{username}" created with the initial password: "{password}".')

    def _create_appuser(self):
        username = os.environ.get('INITIAL_APP_USERNAME')
        password = os.environ.get('INITIAL_APP_PASSWORD')

        try:
            user_models.AppUser.objects.get(email=username)
        except user_models.AppUser.DoesNotExist:
            user_models.AppUser.objects.create(
                email=username,
                password=hashers.make_password(password),
            )
            print(f'App user "{username}" created with the initial password: "{password}".')
