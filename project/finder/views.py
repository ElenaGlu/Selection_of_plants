from django.shortcuts import get_object_or_404, render


from .models import HousePlants
from .forms import CheckBoxForm
from .finder_services import creates_default_filters_for_start_page, generates_page_by_filters, \
    changing_value_of_filters


def displays_plants_by_filters(request):
    if request.method == "GET":
        form = CheckBoxForm(request.POST or None)
        page_number = request.GET.get("page")
        page_obj = generates_page_by_filters(page_number, creates_default_filters_for_start_page())

    if request.method == "POST":
        form = CheckBoxForm(request.POST or None)
        page_number = request.GET.get("page")
        if form.is_valid():
            page_obj = generates_page_by_filters(page_number, changing_value_of_filters(request))

    return render(request, 'finder/filtration_of_plants.html', {'form': form, 'page_obj': page_obj})


def displays_description_of_specific_plant(request, pk):
    plant = get_object_or_404(HousePlants, pk=pk)
    return render(request, 'finder/description_plant.html', {'plant': plant})
