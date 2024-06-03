from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class HomeForm(forms.Form):
    origin = forms.CharField(required=True)
    destination = forms.CharField(required=True)
    passengers = forms.IntegerField(min_value=1, max_value=10)
    departure_date = forms.DateField(widget=DateInput)
    return_date = forms.DateField(widget=DateInput)


