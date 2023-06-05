from django.shortcuts import get_object_or_404, render
from .models import HousePlants
from django.core.paginator import Paginator
from .forms import CheckBoxForm, meth


def select_plant(request):
    form = CheckBoxForm(request.POST or None)
    dict_choice = meth()
    plants = HousePlants.objects.all()
    paginator = Paginator(plants, 30)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if request.method == "POST":
        plants = []
        if form.is_valid():
            level_of_care = request.POST.getlist("level_of_care")
            light_level = request.POST.getlist("light_level")
            irrigation_level = request.POST.getlist("irrigation_level")
            temperature = request.POST.getlist("temperature")
            humidity = request.POST.getlist("humidity")
            feeding = request.POST.getlist("feeding")
            filter_keys = {'level_of_care__in': level_of_care, 'light_level__in': light_level,
                           'irrigation_level__in': irrigation_level, 'temperature__in': temperature,
                           'humidity__in': humidity, 'feeding__in': feeding}

            for key, value in filter_keys.items():
                if not value:
                    filter_keys[key] = dict_choice[key]
            plants = HousePlants.objects.filter(**filter_keys)
        else:
            CheckBoxForm()
        paginator = Paginator(plants, 30)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

    return render(request, 'finder/select_plant.html', {'form': form, 'page_obj': page_obj})


def description_plant(request, pk):
    plant = get_object_or_404(HousePlants, pk=pk)
    return render(request, 'finder/description_plant.html', {'plant': plant})

