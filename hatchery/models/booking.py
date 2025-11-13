from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .property import Property
from .user import User

class Booking(models.Model):
    """ Represents orders for products or services """
    review_id = models.UUIDField(primary_key=True)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, to_field='property_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='user_id')
    rating = models.IntegerField(null=False, validators=[
        MinValueValidator(1),
        MaxValueValidator(2)
    ])
    comment = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
