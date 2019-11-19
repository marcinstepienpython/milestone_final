# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Bid
from auctionPal.forms import BidForm


def bid_list(request):
    bids = Bid.objects.all().order_by('-id')
    context = {
        'bids': bids
    }
    return render(request, 'bids/snippets/bids.html', context)


def bid_new(request, pk):
    form = BidForm()

    return render(request, 'bids/snippets/new.html', {'form': form})
