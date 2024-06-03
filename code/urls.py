from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main_homepage'),
    path('about/', views.about, name="main_about")
]
