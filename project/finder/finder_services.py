from .models import HousePlants

from django.core.paginator import Paginator


def creates_filters() -> dict:
    basic_filters_for_start_page = {'level_of_care': [], 'light_level': [], 'irrigation_level': [],
                                    'temperature': [], 'humidity': [], 'feeding': []}
    for elem in HousePlants.objects.all():
        for key in basic_filters_for_start_page.keys():
            basic_filters_for_start_page[key].append(elem.__dict__[key])
    for key, value in basic_filters_for_start_page.items():
        selection_unique_values = set(value)
        values_for_checkbox_form = tuple((item, item) for item in selection_unique_values)
        basic_filters_for_start_page[key] = values_for_checkbox_form
    return basic_filters_for_start_page


def unpacking_filters() -> dict:
    basic_filters_for_start_page = creates_filters()
    basic_filters_for_start_page = {key: [v[0] for v in values] for key, values in basic_filters_for_start_page.items()}

    full_filter = {
        'level_of_care__in': basic_filters_for_start_page['level_of_care'],
        'light_level__in': basic_filters_for_start_page['light_level'],
        'irrigation_level__in': basic_filters_for_start_page['irrigation_level'],
        'temperature__in': basic_filters_for_start_page['temperature'],
        'humidity__in': basic_filters_for_start_page['humidity'],
        'feeding__in': basic_filters_for_start_page['feeding']
    }
    return full_filter


def pagination_of_pages(request):
    full_filter = unpacking_filters()
    plants = HousePlants.objects.filter(**full_filter)
    paginator = Paginator(plants, 30)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return page_obj


creates_filters()
unpacking_filters()
pagination_of_pages()
