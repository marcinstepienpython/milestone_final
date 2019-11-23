# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Cart
from artifacts.models import Artifact
from orders.models import Order
from billing.models import BillingProfile
from accounts.forms import LoginForm, GuestForm
from accounts.models import GuestEmail
from addresses.forms import AddressForm
from addresses.models import Address

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

    # user = request.user
    # billing_profile = None
    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()

    shipping_address_id = request.session.get('shipping_address_id', None)

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(
        request)

    # check if order doesnt exist
    if billing_profile is not None:
        order_qs = Order.objects.filter(
            billing_profile=billing_profile, cart=cart_obj, active=True)

        order_obj, order_object_created = BillingProfile.objects.new_or_get(
            request)
        

        if order_qs.count() == 1:
            order_obj = order_qs.first()
            # print('2', order_obj.shipping_address)

        else:
            old_order_qs = Order.objects.exclude(
                billing_profile=billing_profile).filter(cart=cart_obj, active=True)
            if old_order_qs.exists():
                old_order_qs.update(active=False)

            order_obj = Order.objects.create(
                billing_profile=billing_profile, cart=cart_obj)
        
        if shipping_address_id:
    
            order_obj.shipping_address = Address.objects.get(
                id=shipping_address_id)
            # print('order_obj.shipping_address', order_obj.shipping_address)
            
            # delete the session
            del request.session['shipping_address_id']
        
        if shipping_address_id:
            # print('1', order_obj.shipping_address)
            order_obj.save()

    if request.method == 'POST':
        is_prepared = order_obj.check_done()
        if is_prepared:
            charged, charge_message = billing_profile.charge(order_obj)
            if charged:
                order_obj.mark_paid()
                del request.session['cart_id']
                return redirect('cart:success')
            else:
                pass
                print(charge_message)
                return redirect("cart:checkout")
            

    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "guest_form": guest_form,
        "address_form": address_form,
        # "billing_address_form":address_form,
    }

    return render(request, 'carts/checkout.html', context)

def checkout_done_view(request):
    return render(request, 'carts/checkout-done.html', {})
