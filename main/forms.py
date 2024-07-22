from django import forms


class Search(forms.Form):
    origin = forms.CharField(label="Origin")
    destination = forms.CharField(label="Destination")
    # departure = forms.


