# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import stripe

intent = stripe.PaymentIntent.create(
    amount=1099,
    currency='eur',
)

stripe.api_key = 'sk_live_tV5por3kAUdEdY8s1HKl8Xn000MuhyijF6'
STRIPE_PUB_KEY = 'pk_live_afCpZiYNkFuVIMYQHcQm926f00udm1y6TC'


def payment_method_view(request):
    if request.method == "POST":
        print(request.POST)

    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY, 'clientSecret': intent.client_secret})
