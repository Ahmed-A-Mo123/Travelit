from django.http import HttpResponse 
from django.http import JsonResponse
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
                "passengers": form.cleaned_data['passengers'],
                "departure_date": form.cleaned_data['departure_date'],
                "return_date": form.cleaned_data['return_date'],
                
            }
            date_check = SearchValidation([content['departure_date'], content['return_date']])

            try:
                date_check.is_date_valid()
            except ValueError as e:
                print({e})
                return render(request, 'error.html', content)
            
            return render(request, 'results.html', content)


    else:
        form = Search()
        return render(request, 'home.html', {"form": form})


def api_request(request):
    if request.method == 'POST':
        # get all the user input details
        
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        passengers = request.POST.get('passengers')
        departure_date = request.POST.get('departure_date')
        return_date = request.POST.get('return_date')
        

        Sky_request = SkyscannerApi(origin, destination, passengers, departure_date, return_date)
        flights = Sky_request.flights()
        return JsonResponse(flights)





def about(request):
    return render(request, 'about.html')
