from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404

from .finder_services import Filters
from .models import HousePlants
from .forms import CheckBoxForm


def displays_plants_by_filters(request: HttpRequest) -> HttpResponse:
    """
    Displays plants by filters.
    param request: http request
    :return: HTML page with plants by filters
    """
    form = CheckBoxForm(request.POST or None)
    page_number = request.GET.get("page")
    if request.method == "GET":
        obj_filter = Filters()
        page_obj = obj_filter.generates_page_by_filters(page_number, obj_filter.creates_default_filters_for_start_page())
    if request.method == "POST":
        if form.is_valid():
            obj_filter = Filters()
            page_obj = obj_filter.generates_page_by_filters(page_number, obj_filter.changing_value_of_filters(request))

    return render(request, 'finder/filtration_of_plants.html', {'form': form, 'page_obj': page_obj})


def displays_description_of_specific_plant(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Displays description of specific plant.
    param request: http request
    param pk: int
    :return: HTML page with description of specific plant
    """
    try:
        plant = HousePlants.objects.get(pk=pk)
    except HousePlants.DoesNotExist:
        raise Http404()
    return render(request, 'finder/description_plant.html', {'plant': plant})
