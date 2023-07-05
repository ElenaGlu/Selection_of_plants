from django.shortcuts import get_object_or_404, render


from .models import HousePlants
from .forms import CheckBoxForm
from .finder_services import creates_default_filters_for_start_page, pagination_of_pages, \
    changing_page_by_checkbox_filters


def select_plant(request):
    page_number = request.GET.get("page")
    page_obj = pagination_of_pages(page_number, creates_default_filters_for_start_page())

    form = CheckBoxForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            changing_page_by_checkbox_filters(request)
        else:
            CheckBoxForm()
            page_obj = pagination_of_pages(page_number, changing_page_by_checkbox_filters)

    return render(request, 'finder/select_plant.html', {'form': form, 'page_obj': page_obj})


def description_plant(request, pk):
    plant = get_object_or_404(HousePlants, pk=pk)
    return render(request, 'finder/description_plant.html', {'plant': plant})
