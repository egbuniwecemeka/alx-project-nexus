from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4

USER_ROLES = (
    ('guest', 'Guest'),
    ('member', 'Member'),
    ('host', 'Host')
)


class User(AbstractUser):
    """ Default user class """
    user_id = models.UUIDField(max_length=90, primary_key=True, default=uuid4, editable=False)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='guest')
    created_at = models.DateTimeField(auto_now_add=True)
