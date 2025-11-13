from django.db import models
from .booking import Booking

PAYMENT_METH = (
    ('credit', 'Credit Card'),
    ('paypal', 'Paypal'),
    ('stripe', 'Stripe')
)


class Payment(models.Model):
    """ payments for booked products or services"""
    payment_id = models.UUIDField(primary_key=True)
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE, to_field='booking_id')
    amount = models.DecimalField(null=False)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(choices=PAYMENT_METH, null=False)

