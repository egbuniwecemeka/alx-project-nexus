from django.contrib import admin
from django.urls import path, include
from .views import booking_details, booking_list

urlpatterns = [
    path('', booking_list, name='booking-list'),
    path('<int:pk>', booking_details, name='booking-details'),
]