# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Review


def review_list(request):
    reviews = Review.objects.all().order_by('-id')
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/reviews_list.html', context)
