# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Cart
from artifacts.models import Artifact

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

    cart_obj.total = total
    cart_obj.save()
    return render(request, 'carts/home.html', {})


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
