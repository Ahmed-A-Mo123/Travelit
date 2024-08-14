from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main_homepage'),
    path('flights_request/', views.flights_request, name='flights_request'),
    path('weather_request/', views.weather_request, name='weather_request'),
    path('chatGPT_request/', views.chatGPT_request, name='chatGPT_request'),
    path('about/', views.about, name="main_about")

]
