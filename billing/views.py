# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from billing.models import BillingProfile
import stripe

stripe.api_key = 'sk_test_0B3fJfkQVP9QjRIKejUSPsXZ00d2j5pJT2'
STRIPE_PUB_KEY = 'pk_test_fpcyXSS2P3x8EvV4rA9hTheC004wTnx3KO'


def payment_method_view(request):
    # if request.user.is_authenticated():
    #     billing_profile = request.user.billingprofile
    #     my_customer_id = billing_profile.my_customer_id

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(
        request)

    if not billing_profile:
        return redirect('/cart')

    if request.method == "POST":
        print(request.POST)

    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY})


def payment_method_createview(request):
    if request.method == "POST":
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(
            request)

        if not billing_profile:
            return HttpResponse({"message": "User not found"}, status_code=401)

        token = request.POST.get('token')

        if token is not None:
            customer = stripe.Customer.retrieve(billing_profile.customer_id)
            card_response = customer.sources.create(source=token)
            print(card_response)
        return JsonResponse({'message': 'Success! Card added!'})
    return HttpResponse("error", status_code=401)
