# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from billing.models import BillingProfile

ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping')
)


class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile)
    address_type = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    address_line1 = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    county = models.CharField(max_length=120)
    country = models.CharField(max_length=120, default='Ireland')

    def __str__(self):
        return str(self.billing_profile)

    def get_address(self):
        return "{line1},\n{line2},\n{city},\n{county},\n{country}".format(
            line1=self.address_line1,
            line2=self.address_line2,
            city=self.city,
            county=self.county,
            country=self.country

        )
