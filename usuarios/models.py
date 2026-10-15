from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    documento = models.CharField(max_length=12, unique=True)

    REQUIRED_FIELDS = ['email', 'documento']

    def __str__(self):
        return f"{self.get_full_name()} ({self.username})"

# Create your models here.
