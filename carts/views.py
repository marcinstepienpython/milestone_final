# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Cart
from artifacts.models import Artifact
from orders.models import Order
from billing.models import BillingProfile
from accounts.forms import LoginForm, GuestForm
from accounts.models import GuestEmail

# Create your views here.


def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    # print('New Cart created!')
    return cart_obj


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'carts/home.html', {"cart": cart_obj})


def cart_update(request):
    artifact_id = request.POST.get('artifact_id')
    if artifact_id is not None:
        try:
            artifact_obj = Artifact.objects.get(id=artifact_id)
        except Artifact.DoesNotExist:
            return redirect('cart:home')

        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if artifact_obj in cart_obj.artifacts.all():
            cart_obj.artifacts.remove(artifact_obj)
        else:
            cart_obj.artifacts.add(artifact_obj)
    # return redirect(artifact_obj.get_url())
    return redirect('cart:home')


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.artifacts.count() == 0:
        return redirect('cart:home')

    user = request.user
    billing_profile = None
    login_form = LoginForm()
    guest_form = GuestForm()
    guest_email_id = request.session.get('guest_email_id')
    if user.is_authenticated():
        if user.email:
            billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(
                user=user, email=user.email)
    
    elif guest_email_id is not None:
        guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
        billing_profile, billing_guest_profile_created = BillingProfile.objects.get_or_create(email=guest_email_obj.email)
    
    else:
        pass

    # check if order doesnt exist
    if billing_profile is not None:
        order_qs = Order.objects.filter(billing_profile=billing_profile, cart=cart_obj, active=True)
        if order_qs.count()==1:
            order_obj = order_qs.first()
        else:
            old_order_qs = Order.objects.exclude(billing_profile=billing_profile).filter(cart=cart_obj, active=True)
            if old_order_qs.exists():
                old_order_qs.update(active=False)

            order_obj = Order.objects.create(billing_profile=billing_profile, cart=cart_obj)

    


    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "guest_form":guest_form
    }

    return render(request, 'carts/checkout.html', context)
