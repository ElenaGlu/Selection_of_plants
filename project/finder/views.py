from django.shortcuts import get_object_or_404, render
from .models import HousePlants


def select_plant(request):
    plants = HousePlants.objects.all()

    return render(request, 'finder/select_plant.html', {'plants': plants})
