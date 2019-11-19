# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Bid


def bid_list(request):
    bids = Bid.objects.all()
    context = {
        'bids': bids
    }
    return render(request, 'bids/snippets/bids.html', context)
