from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import HousePlants
from .forms import CheckBoxForm, filters_form


def select_plant(request):

    dict_filters = filters_form()
    dict_filters = {key: [v[0] for v in values] for key, values in dict_filters.items()}

    form = CheckBoxForm(request.POST or None)
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

            selection = {
                'level_of_care__in': level_of_care if level_of_care else dict_filters['level_of_care'],
                'light_level__in': light_level if light_level else dict_filters['light_level'],
                'irrigation_level__in': irrigation_level if irrigation_level else dict_filters['irrigation_level'],
                'temperature__in': temperature if temperature else dict_filters['temperature'],
                'humidity__in': humidity if humidity else dict_filters['humidity'],
                'feeding__in': feeding if feeding else dict_filters['feeding']
            }
            plants = HousePlants.objects.filter(**selection)
        else:
            CheckBoxForm()
        paginator = Paginator(plants, 30)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

    return render(request, 'finder/select_plant.html', {'form': form, 'page_obj': page_obj})


def description_plant(request, pk):
    plant = get_object_or_404(HousePlants, pk=pk)
    return render(request, 'finder/description_plant.html', {'plant': plant})
