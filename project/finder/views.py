from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpRequest
from django.core.exceptions import BadRequest

from .models import HousePlants
from .forms import CheckBoxForm

#TODO множественные импорты
from services import finder_services as fs
from services import second_services as fs


#TODO комментарий
def displays_plants_by_filters(request: HttpRequest) -> HttpResponse:
    """
    Displays plants by filters
    :param request: http request

    :return:
    """
    form = CheckBoxForm(request.POST or None)
    page_number = request.GET.get("page")
    if request.method == "GET":
        page_obj = fs.generates_page_by_filters(page_number, fs.creates_default_filters_for_start_page())
    if request.method == "POST":
        if form.is_valid():
            page_obj = fs.generates_page_by_filters(page_number, fs.changing_value_of_filters(request))
    # else:
    #     raise BadRequest('Ты не туда воеюшь дурачок')
        # return HttpResponse(status=406, content='Method not allowed')
    return render(request, 'finder/filtration_of_plants.html', {'form': form, 'page_obj': page_obj})


#TODO Аннотации типов + комментарий
def displays_description_of_specific_plant(request, pk):
    if request.method == 'POST':
        plant = get_object_or_404(HousePlants, pk=pk)
    else:
        # raise BadRequest('Ты не туда воеюшь дурачок')
        return HttpResponse(status=406, content='Method not allowed')
    return render(request, 'finder/description_plant.html', {'plant': plant})


