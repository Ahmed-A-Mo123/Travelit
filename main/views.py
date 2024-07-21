from django.http import HttpResponse
from django.shortcuts import render

from main.back_end.api_manager import Chatgpt
from main.back_end.api_manager import SkyscannerApi


# Create your views here.
def home(request):
    # sky = SkyscannerApi('london', 'New york', '2', '2024-02-13', '2024-02-20')
    # context = {
    #     'flights': sky.flights(),
    # }
    return render(request, 'home.html')



def about(request):
    return render(request, 'main/about.html')

