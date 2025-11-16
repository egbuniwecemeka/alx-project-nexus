from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from uuid import uuid4
from .property import Property
from .user import User

BOOK_STATUS = (
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('canceled', 'Canceled'),
)

class Booking(models.Model):
    """ Represents orders for products or services """
    booking_id = models.UUIDField(primary_key=True, default=uuid4)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, to_field='property_id') # Later edited for its specific service
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='user_id')
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    status = models.CharField(max_length=15, choices=BOOK_STATUS, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
