from django.http import HttpResponse
from django.shortcuts import render
from .forms import Search

from main.back_end.api_manager import Chatgpt
from main.back_end.api_manager import SkyscannerApi


# Create your views here.
def home(request):
    # sky = SkyscannerApi('london', 'New york', '2', '2024-02-13', '2024-02-20')
    # context = {
    #     'flights': sky.flights(),
    # }

    if request.method == 'POST':
        form = Search(request.POST)
        if form.is_valid():
            origin = form.cleaned_data['origin']
            destination = form.cleaned_data['destination']
            departure_date = form.cleaned_data['departure_date']
            return_date = form.cleaned_data['return_date']
            print(origin, destination, departure_date,return_date)
    else:
        form = Search()
        return render(request, 'home.html', {"form": form})




def about(request):
    return render(request, 'main/about.html')

