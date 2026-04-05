from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('VIEWER', 'Viewer'),
        ('ANALYST', 'Analyst'),
        ('ADMIN', 'Admin'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)