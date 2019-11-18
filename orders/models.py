# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from carts.models import Cart

from django.db.models.signals import post_save

# Create your models here.


class Order(models.Model):
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=120, default='created')
    total = models.DecimalField(default=0.00, max_digits=30, decimal_places=2)

    def __str__(self):
        return str(self.id)

    def update_total(self):
        cart_total = self.cart.total
        shipping_total = 50  # 50 Euro standard shipping price
        new_total = cart_total + shipping_total
        self.total = new_total
        self.save()
        return new_total


def post_save_cart_total(sender, instance, created, *args, **kwargs):

    if not created:
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()


post_save.connect(post_save_cart_total, sender=Cart)


def post_save_order(sender, instance, created, *args, **kwargs):
    if created:
        instance.update_total()


post_save.connect(post_save_order, sender=Order)