# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import stripe

stripe.api_key = 'sk_test_0B3fJfkQVP9QjRIKejUSPsXZ00d2j5pJT2'
STRIPE_PUB_KEY = 'pk_test_fpcyXSS2P3x8EvV4rA9hTheC004wTnx3KO'


def payment_method_view(request):
    if request.method == "POST":
        print(request.POST)

    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY})


def payment_method_createview(request):
    if request.method == "POST":
        return JsonResponse({'message': 'Success! Card added!'})
    return HttpResponse("error", status_code=401)
