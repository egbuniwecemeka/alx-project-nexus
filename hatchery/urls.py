from django.contrib import admin
from django.urls import path
from . import views


app_name = 'hatchery'

urlpatterns = [
    path('', views.home, name='home'),
    path('create-checkout-session/', views.create_checkout_session, name='checkout'),
    path('booking/', views.booking, name='booking'),
]