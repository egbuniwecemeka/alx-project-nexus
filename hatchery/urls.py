from django.contrib import admin
from rest_framework.urls import path, include
from .views import booking_details, booking_list

URLPATTERNS = [
    path('booking/', booking_list, name='booking-list'),
    path('booking/<int:pk>', booking_details, name='booking-details'),
]