from django.db import models
from uuid import uuid4
from .user import User


class Message(models.Model):
    """ Represents conversations amongst users """
    message_id = models.UUIDField(primary_key=True, default=uuid4)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='user_id',
                                  related_name='sent_messages')
    recipient_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='user_id',
                                     related_name='received_messages')
    message_body = models.TextField(null=False)
    sent_at = models.DateTimeField(auto_now_add=True)
