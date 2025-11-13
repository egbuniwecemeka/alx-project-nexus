""" Serialization of models data  """

from rest_framework import serializers
from .models.user import User
from .models.booking import Booking
from .models.message import Message
from .models.payment import Payment
from .models.property import Property
from models.review import Review


class UserSerializer(serializers.ModelSerializer):
    """ User model serializer """

    class Meta:
        model = User
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    """ Property model serializer"""

    class Meta:
        model = Property
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    """ Booking model serializer"""

    class Meta:
        model = Booking
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    """ Message model serializer"""

    class Meta:
        model = Message
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    """ Payment model serializer"""

    class Meta:
        model = Payment
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    """ Review model serializer"""

    class Meta:
        model = Review
        fields = '__all__'
