from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import HousePlants
from .forms import CheckBoxForm
from .finder_services import creates_filters, unpacking_filters, pagination_of_pages


def select_plant(request):
    page_obj = pagination_of_pages(request)
    form = CheckBoxForm(request.POST or None)
    if request.method == "POST":
        plants = []
        if form.is_valid():
            level_of_care = request.POST.getlist("level_of_care")
            light_level = request.POST.getlist("light_level")
            irrigation_level = request.POST.getlist("irrigation_level")
            temperature = request.POST.getlist("temperature")
            humidity = request.POST.getlist("humidity")
            feeding = request.POST.getlist("feeding")

            basic_filters_for_start_page = creates_filters()

            selection = {
                'level_of_care__in': level_of_care if level_of_care else basic_filters_for_start_page['level_of_care'],
                'light_level__in': light_level if light_level else basic_filters_for_start_page['light_level'],
                'irrigation_level__in': irrigation_level if irrigation_level else basic_filters_for_start_page[
                    'irrigation_level'],
                'temperature__in': temperature if temperature else basic_filters_for_start_page['temperature'],
                'humidity__in': humidity if humidity else basic_filters_for_start_page['humidity'],
                'feeding__in': feeding if feeding else basic_filters_for_start_page['feeding']
            }
            plants = HousePlants.objects.filter(**selection)
            paginator = Paginator(plants, 30)
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)

        else:
            CheckBoxForm()
            page_obj = pagination_of_pages(request)

    return render(request, 'finder/select_plant.html', {'form': form, 'page_obj': page_obj})


def description_plant(request, pk):

    plant = get_object_or_404(HousePlants, pk=pk)
    return render(request, 'finder/description_plant.html', {'plant': plant})
