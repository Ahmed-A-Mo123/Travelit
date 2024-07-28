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
    # test = forms.DateTimeField(widget= forms.DateInput( attrs= {
    #     # 'class': 'form-control',
    #     'type': 'date'
    # }))
    departure_date = forms.DateTimeField(widget=forms.DateInput(attrs={
        'class': 'border rounded date-pick-input',
        'type': 'date'
    }), required=True)
    return_date = forms.DateTimeField(widget=forms.DateInput(attrs={
        'class': 'border rounded date-pick-input',
        'type': 'date'
    }), required=True, label="return")
