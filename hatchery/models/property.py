from django.db import models
from .user import User
from uuid import uuid4


class Property(models.Model):
    """  Represents poultry properties or farm units """
    property_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    host_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='user_id')
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    location = models.CharField(max_length=40, null=False)
    priceperbird = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
