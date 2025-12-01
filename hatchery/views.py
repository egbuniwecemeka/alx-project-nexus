""" Views models for handling CRUD operations """

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

# Homepage view
def home(request):
    return render(request, 'hatchery/home.html')

# Bookingpage view
def booking(request):
    return render(request, 'hatchery/booking.html')

# Payment success view     Implement later
def success_page(request):
    return render(request, 'hatchery/success.html')

# Payment failure view    Implement later
def failure_page(request):
    return render(request, 'hatchery/failure.html')

# Stripe Checkout Session view
stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    try:
        checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'ngn',
                    'product_data': {
                        'name': 'Broilers',
                    },
                    'unit_amount': 20000 * 100 # Stripe -> Kobo
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='https://ejfarms.onrender.com/success/',
        cancel_url='https://ejfarms.onrender.com/cancel/'
        )
        return JsonResponse({id: checkout_session})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
