from django import forms
from .models import Address

# Address class form


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'address_line1',
            'address_line2',
            'city',
            'county',
            'country'
        ]
