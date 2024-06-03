from django.http import HttpResponse
from django.shortcuts import render
from code.forms import HomeForm

from code.back_end.interface_manager import Search


def api_helper(origin, destination, passengers, departure_date, return_date): # takes in the api parameters and returns api objects
    search_results = Search(origin, destination, passengers, departure_date, return_date)
    return search_results

# Create your views here.
def home(request):
    form = HomeForm()
    context = {'form': form}

    if request.method == 'POST':
        origin = request.POST['origin']
        destination = request.POST['destination']
        passengers = request.POST['passengers']
        departure_date = request.POST['departure_date']
        return_date = request.POST['return_date']

        search = api_helper(origin, destination, passengers, departure_date, return_date)

        context = {
            # 'hotel_list': sky.get_hotel_list(),
            'flights_list': search.get_flight_list()
            # 'hotel_search_status': sky.get_hotel_search_status(),
            # 'user_dates': sky.get_dates(),
            # 'day_count': sky.get_dates()
        }

        return render(request, 'templates/main/about.html', context)
    return render(request, 'templates/main/home.html', context)


def about(request):
    return render(request, 'main/about.html')



# sky = Search('london', 'New york', '2', '2024-05-13', '2024-05-20')
#     # sky.hotels()
#     sky.flights()