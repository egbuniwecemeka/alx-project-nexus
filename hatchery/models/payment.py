from django.db import models
from .booking import Booking
from uuid import uuid4

PAYMENT_METH = (
    ('credit', 'Credit Card'),
    ('paypal', 'Paypal'),
    ('stripe', 'Stripe')
)


class Payment(models.Model):
    """ payments for booked products or services"""
    payment_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE, to_field='booking_id')
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=15, choices=PAYMENT_METH, null=False)
