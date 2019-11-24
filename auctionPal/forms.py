from django import forms
from django.contrib.auth import get_user_model
from bids.models import Bid
from reviews.models import Review
# from django.db.models import Max

User = get_user_model()


class BidForm(forms.ModelForm):

    class Meta:
        model = Bid
        fields = ('offer',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'review')
