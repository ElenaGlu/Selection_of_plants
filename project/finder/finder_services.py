from .models import HousePlants

from django.core.paginator import Paginator


def creates_filters_for_form_checkbox() -> dict:
    """
    Функция создает словарь для чекбоксформ, и заполняет его уникальными значениями в виде кортежа.
    :return: словарь, где ключ-название фильтра, значение-варианты выбора.
    """
    filters_for_form_checkbox = {'level_of_care': [], 'light_level': [], 'irrigation_level': [],
                                 'temperature': [], 'humidity': [], 'feeding': []}
    for elem in HousePlants.objects.all():
        for key in filters_for_form_checkbox.keys():
            filters_for_form_checkbox[key].append(elem.__dict__[key])
    for key, value in filters_for_form_checkbox.items():
        selection_unique_values = set(value)
        values_for_checkbox_form = tuple((item, item) for item in selection_unique_values)
        filters_for_form_checkbox[key] = values_for_checkbox_form
    return filters_for_form_checkbox


def creates_default_filters_for_start_page() -> dict:
    """
    Функция создает фильтры по умолчанию для стартовой страницы.
    :return: словарь, где ключ-название фильтра, значение-варианты выбора.
    """
    filters_for_form_checkbox = creates_filters_for_form_checkbox()
    filters_for_form_checkbox = {key: [v[0] for v in values] for key, values in
                                 filters_for_form_checkbox.items()}

    default_filters_for_start_page = {
        'level_of_care__in': filters_for_form_checkbox['level_of_care'],
        'light_level__in': filters_for_form_checkbox['light_level'],
        'irrigation_level__in': filters_for_form_checkbox['irrigation_level'],
        'temperature__in': filters_for_form_checkbox['temperature'],
        'humidity__in': filters_for_form_checkbox['humidity'],
        'feeding__in': filters_for_form_checkbox['feeding']
    }
    return default_filters_for_start_page


def changing_page_by_checkbox_filters(request) -> dict:
    level_of_care = request.POST.getlist("level_of_care")
    light_level = request.POST.getlist("light_level")
    irrigation_level = request.POST.getlist("irrigation_level")
    temperature = request.POST.getlist("temperature")
    humidity = request.POST.getlist("humidity")
    feeding = request.POST.getlist("feeding")

    filters_for_form_checkbox = creates_filters_for_form_checkbox()

    selection = {
        'level_of_care__in': level_of_care if level_of_care else filters_for_form_checkbox['level_of_care'],
        'light_level__in': light_level if light_level else filters_for_form_checkbox['light_level'],
        'irrigation_level__in': irrigation_level if irrigation_level else filters_for_form_checkbox[
            'irrigation_level'],
        'temperature__in': temperature if temperature else filters_for_form_checkbox['temperature'],
        'humidity__in': humidity if humidity else filters_for_form_checkbox['humidity'],
        'feeding__in': feeding if feeding else filters_for_form_checkbox['feeding']
    }
    return selection


def pagination_of_pages(page_number, dict_with_filter):
    plants = HousePlants.objects.filter(**dict_with_filter)
    paginator = Paginator(plants, 30)
    page_obj = paginator.get_page(page_number)

    return page_obj
