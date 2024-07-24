from django import forms
from .models import SearchFields


class Search(forms.Form):
    origin = forms.CharField(label="Origin", required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Origin',
    }))
    destination = forms.CharField(label="Destination", required=True, widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Destination'
    }))
    departure_date = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing", attrs={
        'class': 'form-select'
    }), required=True)
    return_date = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing", attrs={
        'class': 'form-select'
    }), required=True)
