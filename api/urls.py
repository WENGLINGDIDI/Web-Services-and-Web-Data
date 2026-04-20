from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weather_list),
    path('weather/<int:pk>/', views.weather_detail),
    path('weather/temStats/', views.weather_temStats),
    path('weather/search/', views.weather_search),
]