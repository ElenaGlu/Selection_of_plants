from django.shortcuts import get_object_or_404, render
from .models import HousePlants
from django.core.paginator import Paginator
from .forms import CheckBoxForm


def select_plant(request):
    form = CheckBoxForm(request.POST or None)
    plants = HousePlants.objects.all()
    paginator = Paginator(plants, 30)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if request.method == "POST":
        plants = []
        if form.is_valid():
            level_of_care = request.POST.getlist("level_of_care")
            plants = HousePlants.objects.filter(level_of_care__in=level_of_care)


            light_level = request.POST.getlist("light_level")
            plants2 = HousePlants.objects.filter(light_level__in=light_level)
            plants.extend(plants2)

            irrigation_level = request.POST.getlist("irrigation_level")
            plants3 = HousePlants.objects.filter(irrigation_level__in=irrigation_level)
            plants.extend(plants3)

            temperature = request.POST.getlist("temperature")
            plants4 = HousePlants.objects.filter(temperature__in=temperature)
            plants.extend(plants4)

            humidity = request.POST.getlist("humidity")
            plants5 = HousePlants.objects.filter(humidity__in=humidity)
            plants.extend(plants5)

            feeding = request.POST.getlist("feeding")
            plants6 = HousePlants.objects.filter(feeding__in=feeding)
            plants.extend(plants6)

        else:
            CheckBoxForm()
        paginator = Paginator(plants, 30)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

    return render(request, 'finder/select_plant.html', {'form': form, 'page_obj': page_obj})
