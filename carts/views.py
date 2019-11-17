# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Cart

# Create your views here.


def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    # print('New Cart created!')
    return cart_obj


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    artifacts = cart_obj.artifacts.all()
    total = 0
    for x in artifacts:

        total += x.price
    print('total:', total)
    cart_obj.total = total
    cart_obj.save()
    return render(request, 'carts/home.html', {})
