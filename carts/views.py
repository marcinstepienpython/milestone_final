# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def cart_home(request):
    cart_id = request.session.get('cart_id', None)
    if cart_id is None: #and isinstance(cart_id, int):
        print('create a new cart!')
    else:
        print('CartID exists')
    return render(request, 'carts/home.html', {})
