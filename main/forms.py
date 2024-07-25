from django import forms
from .models import SearchFields


class Search(forms.Form):
    origin = forms.CharField(label="Origin", required=True, widget=forms.TextInput(attrs={
        'class': 'border rounded search-input',
        'placeholder': 'Enter Origin',
    }))
    destination = forms.CharField(label="Destination", required=True, widget= forms.TextInput(attrs={
        'class': 'border rounded search-input',
        'placeholder': 'Enter Destination'
    }))
    departure_date = forms.DateField(widget=forms.SelectDateWidget(empty_label="Departure Date", attrs={
        'class': 'border rounded date-pick-input'
    }), required=True)
    return_date = forms.DateField(widget=forms.SelectDateWidget(empty_label="", attrs={
        'class': 'border rounded date-pick-input'
    }), required=True, label="return")
