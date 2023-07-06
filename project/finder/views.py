from django.shortcuts import get_object_or_404, render

from .models import HousePlants
from .forms import CheckBoxForm
from .finder_services import creates_default_filters_for_start_page, generates_page_by_filters, \
    changing_value_of_filters


def select_plant(request):
    form = CheckBoxForm(request.POST or None)
    page_number = request.GET.get("page")
    page_obj = generates_page_by_filters(page_number, creates_default_filters_for_start_page())

    if request.method == "POST":
        form = CheckBoxForm(request.POST or None)
        if form.is_valid():
            page_obj = generates_page_by_filters(page_number, changing_value_of_filters(request))
        else:
            print(form.errors)

    return render(request, 'finder/select_plant.html', {'form': form, 'page_obj': page_obj})


def description_plant(request, pk):
    plant = get_object_or_404(HousePlants, pk=pk)
    return render(request, 'finder/description_plant.html', {'plant': plant})
