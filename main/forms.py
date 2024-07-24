from django import forms


class Search(forms.Form):
    origin = forms.CharField(label="Origin", required=True)
    destination = forms.CharField(label="Destination", required=True)
    departure_date = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"), required=True)
    return_date = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"), required=True)
