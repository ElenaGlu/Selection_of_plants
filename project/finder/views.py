from django.shortcuts import render
from django.http import Http404
from .models import HousePlants


def select_plant(request):
    plants = HousePlants.name_of_plant
    return render(request, 'select_plant.html', {'plants': plants})
