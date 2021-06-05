from django.contrib.auth import models as dj_models
from django.db import models
import uuid


class AppUser(dj_models.AbstractBaseUser):
    class Meta:
        db_table = 'user_app'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    objects = dj_models.UserManager()

    @property
    def username(self):
        return self.email

    @property
    def is_staff(self):
        return False

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()

    def __str__(self):
        return self.email
