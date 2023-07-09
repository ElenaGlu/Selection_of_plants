from .models import HousePlants

from django.core.paginator import Paginator


def creates_filters_for_checkbox_form() -> dict:
    """
    Функция создает словарь для чекбоксформ, и заполняет его уникальными значениями в виде кортежа.
    :return: словарь, где ключ-название фильтра, значение-варианты выбора.
    """
    #TODO оптимизировать
    # https://stackoverflow.com/questions/20135343/django-unique-filtering
    # + попробовать чистым sql "select distinct *name of column* from *table* wat";
    # пример чистого sql https://github.com/GluhovDmitry/electro-wallet/blob/master/wallet_app/handlers/ratings_handler.py
    # замерить время выполнения (модуль time)
    filters_for_checkbox_form = {'level_of_care': [], 'light_level': [], 'irrigation_level': [],
                                 'temperature': [], 'humidity': [], 'feeding': []}
    for elem in HousePlants.objects.all():
        for key in filters_for_checkbox_form.keys():
            filters_for_checkbox_form[key].append(elem.__dict__[key])
    for key, value in filters_for_checkbox_form.items():
        selection_unique_values = set(value)
        values_for_checkbox_form = tuple((item, item) for item in selection_unique_values)
        filters_for_checkbox_form[key] = values_for_checkbox_form
    return filters_for_checkbox_form


def dictionary_conversion() -> dict:
    """
    Функция преобразует значения ключей из кортежа в список.
    :return: словарь
    """
    default_filters = creates_filters_for_checkbox_form()
    return {key: [v[0] for v in values] for key, values in default_filters.items()}


def creates_default_filters_for_start_page() -> dict:
    """
    Функция создает фильтры по умолчанию для стартовой страницы.
    :return: словарь, где ключ-название фильтра, значение-варианты выбора.
    """
    #TODO вызываешь это два раза, лучше вызови раньше и передай в параметрах
    default_filters = dictionary_conversion()
    # default_filters_for_start_page = {
    #     'level_of_care__in': default_filters['level_of_care'],
    #     'light_level__in': default_filters['light_level'],
    #     'irrigation_level__in': default_filters['irrigation_level'],
    #     'temperature__in': default_filters['temperature'],
    #     'humidity__in': default_filters['humidity'],
    #     'feeding__in': default_filters['feeding']
    # }
    default_filters_for_start_page = {f'{k}__in': v for k, v in default_filters.items()}
    return default_filters_for_start_page


def changing_value_of_filters(request) -> dict:
    """
    Функция получает запрос из форм чекбокса и меняет варианты значений словаря и возвращет новый словарь.
    :return: словарь, где ключ-название фильтра, значение-варианты выбора.
    """
    # level_of_care = request.POST.getlist("level_of_care")
    # light_level = request.POST.getlist("light_level")
    # irrigation_level = request.POST.getlist("irrigation_level")
    # temperature = request.POST.getlist("temperature")
    # humidity = request.POST.getlist("humidity")
    # feeding = request.POST.getlist("feeding")

    default_filters = dictionary_conversion()

    # modified_filters = {
    #     'level_of_care__in': level_of_care if level_of_care else default_filters['level_of_care'],
    #     'light_level__in': light_level if light_level else default_filters['light_level'],
    #     'irrigation_level__in': irrigation_level if irrigation_level else default_filters[
    #         'irrigation_level'],
    #     'temperature__in': temperature if temperature else default_filters['temperature'],
    #     'humidity__in': humidity if humidity else default_filters['humidity'],
    #     'feeding__in': feeding if feeding else default_filters['feeding']
    # }
    modified_filters = {f'{k}__in': request.POST.getlist(k) if request.POST.getlist(k) else v for k, v in default_filters.items()}
    return modified_filters


def generates_page_by_filters(page_number, dict_with_filter):
    """
    Функция выводит объекты на страницу, исходя из полученных фильтров.
    Используется пагинация для формирования страниц.
    :return: объекты
    """
    obj = HousePlants.objects.filter(**dict_with_filter)
    paginator = Paginator(obj, 30)
    page_obj = paginator.get_page(page_number)

    return page_obj
