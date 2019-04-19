from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('weather/<int:pk>/', views.weather_detail, name='weather_detail'),
	path('weather/new/', views.weather_new, name='weather_new'),
	path('weather/<int:pk>/edit/', views.weather_edit, name='weather_edit'),
	path('weather/<int:pk>/delete/', views.weather_delete, name='weather_delete'),
]	