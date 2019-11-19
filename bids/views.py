# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Bid
from artifacts.models import Artifact
from auctionPal.forms import BidForm


def bid_list(request):
    bids = Bid.objects.all().order_by('-id')
    context = {
        'bids': bids
    }
    return render(request, 'bids/snippets/bids.html', context)


def bid_new(request, pk):
    if request.method == 'POST':
        artifact = Artifact.objects.filter(pk=pk).first()
        form = BidForm(request.POST)

        if form.is_valid():
            bid = form.save(commit=False)
            bid.user = request.user
            bid.artifact = artifact

            bid.save()
            return redirect('details', pk=pk)
        else:

            return render(request, 'bids/snippets/new.html', {'form': form})

    else:
        form = BidForm()

    return render(request, 'bids/snippets/new.html', {'form': form})
