from django.db import models

# overriding the adstract user
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    #
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email
