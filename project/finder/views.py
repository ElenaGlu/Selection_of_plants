from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404

from .finder_services import Filters
from .models import HousePlants
from .forms import CheckBoxForm


def displays_plants_by_filters(request: HttpRequest) -> HttpResponse:
    """
    Displays plants by filters.
    :param request: Http Request
    :return: HTML page with plants by filters
    """
    obj_filter = Filters()
    choices_for_widgets = obj_filter.creates_choices_for_widgets()
    dictionary_with_filters = obj_filter.converts_dictionary(choices_for_widgets)

    form = CheckBoxForm(request.POST or None)
    page_number = request.GET.get("page")
    if request.method == "GET":
        default_filter = obj_filter.creates_default_filters_for_start_page(dictionary_with_filters)
        page_obj = obj_filter.generates_page_by_filters(
            page_number,
            default_filter
        )
    if request.method == "POST":
        if form.is_valid():
            changing_filter = obj_filter.changing_value_of_filters(request.POST, dictionary_with_filters)
            page_obj = obj_filter.generates_page_by_filters(
                page_number, changing_filter
            )

    return render(request, 'finder/filtration_of_plants.html', {'form': form, 'page_obj': page_obj})


def displays_description_of_specific_plant(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Displays description of specific plant.
    :param request: Http Request
    :param pk: id object in data base
    :return: HTML page with description of specific plant
    """
    try:
        plant = HousePlants.objects.get(pk=pk)
    except HousePlants.DoesNotExist:
        raise Http404()
    return render(request, 'finder/description_plant.html', {'plant': plant})
