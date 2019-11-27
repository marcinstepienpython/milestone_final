# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from billing.models import BillingProfile, Card
import stripe
import os
import env

stripe.api_key = os.environ.get('STRIPE_SECRET')
STRIPE_PUB_KEY = os.environ.get('STRIPE_PUB_KEY')


# payment method view
def payment_method_view(request):


    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(
        request)

    if not billing_profile:
        return redirect('/cart')

    if request.method == "POST":
        pass

    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY})

# create card view
def payment_method_createview(request):
    if request.method == "POST":
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(
            request)

        if not billing_profile:
            return HttpResponse({"message": "User not found"}, status_code=401)

        token = request.POST.get('token')

        if token is not None:
            
            new_card_obj = Card.objects.add_new(billing_profile, token)
            
        return JsonResponse({'message': 'Success! Card added!'})
    return HttpResponse("error", status_code=401)
