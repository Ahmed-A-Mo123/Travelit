from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main_homepage'),
    path('api_request/', views.api_request, name='api_request'),
    path('about/', views.about, name="main_about")

]
