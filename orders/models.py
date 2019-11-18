# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from carts.models import Cart

# Create your models here.


class Order(models.Model):
    order_id = models.CharField(max_length=120, blank=True)
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=120, default='created')
    total = models.DecimalField(default=0.00, max_digits=30, decimal_places=2)

    def __str__(self):
        return self.order_id
