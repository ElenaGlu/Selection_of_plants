from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .app_services import Filter, ContentPlant
from .forms import CheckBoxForm


def filter_plant(request: HttpRequest) -> HttpResponse:
    """
    Filter the list of plants.
    :param:request: Expects an optional 'page' query parameter (e.g., ?page=2).
    :return: Render HTML template containing the filter form and the paginated list of filtered plants.
    """

    page_number = request.GET.get("page")
    form = CheckBoxForm(request.POST or None)
    page_obj = Filter.select_plant(page_number, form)
    return render(request, 'finder/filter_plant.html', {'form': form, 'page_obj': page_obj})


def display_content_plant(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Display detailed information about a specific plant.
    :param:request: HTTP request object.
    :param:pk: The primary key of the plant to be displayed.
    :return: Rendered HTML page containing the plant details
    """
    plant, content = ContentPlant.process_incorrect_info(pk)
    return render(request, 'finder/description_plant.html', {'plant': plant, 'content': content})
