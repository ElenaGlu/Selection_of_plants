from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import HousePlants
from .forms import CheckBoxForm, filters_form


def select_plant(request):
    form = CheckBoxForm(request.POST or None)

    dict_filters = filters_form()

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
                'level_of_care__in': level_of_care if level_of_care else list(dict_filters['level_of_care']),
                'light_level__in': light_level,
                'irrigation_level__in': irrigation_level,
                'temperature__in': temperature,
                'humidity__in': humidity,
                'feeding__in': feeding
            }
            # new_selection = {}
            # list_val = []
            # for key, value in selection.items():
            #     if value:
            #         new_selection.setdefault(key, value)
            # for key1, value1 in dict_filters.items():
            #     if not key1 in new_selection:
            #         for item in value1:
            #             val = item[0]
            #             list_val.append(val)
            #         new_selection.setdefault(key1, list_val)
            #         list_val = []

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
