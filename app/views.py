from .models import *
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .forms import WeatherForm


def index(request):
    weather_list = WeatherList.objects.all()
    context = {'weather_list' : weather_list}
    return render(request, 'app/index.html', context)


def weather_detail(request, pk):
    weather = get_object_or_404(WeatherList, pk=pk)
    return render(request, 'app/weather_detail.html', {'weather': weather})


def weather_new(request):
    if request.method == "POST":
        form = WeatherForm(request.POST)
        if form.is_valid():
            weather = form.save(commit=False)
            weather.save()
            return redirect('weather_detail', pk=weather.pk)
    else:
        form = WeatherForm()
    return render(request, 'app/weather_edit.html', {'form': form})


def weather_edit(request, pk):
    weather = get_object_or_404(WeatherList, pk=pk)
    if request.method == "POST":
        form = WeatherForm(request.POST, instance=weather)
        if form.is_valid():
            weather = form.save(commit=False)
            weather.save()
            return redirect('weather_detail', pk=weather.pk)
    else:
        form = WeatherForm(instance=weather)
    return render(request, 'app/weather_edit.html', {'form': form})


def weather_delete(request, pk):
    weather = WeatherList.objects.get(pk=pk)
    weather.delete()
    return redirect("/")