from django.contrib import admin
from django.urls import path, include
from .views import booking_details, booking_list, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bookings/', booking_list, name='booking-list'),
    path('<int:pk>', booking_details, name='booking-details'),
]