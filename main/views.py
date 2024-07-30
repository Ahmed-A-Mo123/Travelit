from django.http import HttpResponse
from django.shortcuts import render
from .forms import Search

from main.back_end.api_manager import Chatgpt
from main.back_end.api_manager import SkyscannerApi
from main.back_end.error_manager import SearchValidation


# Create your views here.
def home(request):
    # sky = SkyscannerApi('london', 'New york', '2', '2024-02-13', '2024-02-20')
    # context = {
    #     'flights': sky.flights(),
    # }

    if request.method == 'POST':
        form = Search(request.POST)
        if form.is_valid():
            content = {
                "origin": form.cleaned_data['origin'],
                "destination": form.cleaned_data['destination'],
                "departure_date": form.cleaned_data['departure_date'],
                "return_date": form.cleaned_data['return_date']
            }
            date_check = SearchValidation([content['departure_date'], content['return_date']])
            try:
                date_check.is_date_valid()
            except ValueError as e:
                print({e})
                return render(request, 'error.html', content)
            # finish this error handling of wrong date inputs and add the necessary frontend aspects.
            return render(request, 'results.html', content)


    else:
        form = Search()
        return render(request, 'home.html', {"form": form})


def about(request):
    return render(request, 'about.html')
