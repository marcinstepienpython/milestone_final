# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .models import Review
from auctionPal.forms import ReviewForm
from artifacts.models import Artifact

def review_list(request):
    reviews = Review.objects.all().order_by('-id')
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/reviews_list.html', context)

def review_new(request, pk):
    if request.method == 'POST':
        artifact = Artifact.objects.filter(pk=pk).first()
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.artifact = artifact

            review.save()
            return redirect('details', pk=pk)
        else:

            return render(request, 'reviews/new.html', {'form': form})

    else:
        form = ReviewForm()

    return render(request, 'reviews/new.html', {'form': form})