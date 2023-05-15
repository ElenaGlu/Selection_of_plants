from django.shortcuts import get_object_or_404, render
from .models import HousePlants
from django.core.paginator import Paginator


def select_plant(request):
    plants = HousePlants.objects.all()
    paginator = Paginator(plants, 30)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'finder/select_plant.html', {'page_obj': page_obj})

