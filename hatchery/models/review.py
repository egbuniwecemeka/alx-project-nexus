from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .property import Property
from .user import User
from uuid import uuid4


class Review(models.Model):
    """ Shows users reviews based on purchased products """
    review_id = models.UUIDField(primary_key=True, default=uuid4)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, to_field='property_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='user_id')
    rating = models.IntegerField(null=False, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    comment = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
