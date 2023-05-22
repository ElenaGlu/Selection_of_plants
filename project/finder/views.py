from django.shortcuts import get_object_or_404, render
from .models import HousePlants
from django.core.paginator import Paginator
from .forms import CheckBoxForm


def select_plant(request):
    form = CheckBoxForm(request.POST or None)
    plants = HousePlants.objects.all()
    paginator = Paginator(plants, 30)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if request.method == "POST":
        plants = []
        if form.is_valid():
            level_of_care = request.POST["level_of_care"]
            plants = HousePlants.objects.filter(level_of_care=level_of_care)
        else:
            CheckBoxForm()
    paginator = Paginator(plants, 30)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'finder/select_plant.html', {'form': form, 'page_obj': page_obj})
