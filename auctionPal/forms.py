from django import forms
from django.contrib.auth import get_user_model
from bids.models import Bid
# from django.db.models import Max

User = get_user_model()


class BidForm(forms.ModelForm):

    class Meta:
        model = Bid
        fields = ('offer',)



