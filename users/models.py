from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)  # keep username, but enforce unique email
    contact_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username
