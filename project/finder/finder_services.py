from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse

from .models import HousePlants


class Filters:

    @staticmethod
    def creates_choices_for_widgets() -> dict:
        """
        Creates "choices" for widgets (CheckBoxForm) based on unique values from HousePlants.
        :return: Dictionary, where the key is the name of the widget, the value is the options "choices"
                 Example {"level_of_care": (("small", "small"),("medium", "medium"),("high", "high")), }
        """
        choices_for_widgets = {'level_of_care': [], 'light_level': [], 'irrigation_level': [],
                               'temperature': [], 'humidity': [], 'feeding': []}
        choices_for_widgets = {k: HousePlants.objects.all().values_list(k, flat=True).distinct() for k, v in
                               choices_for_widgets.items()}
        return {k: tuple((item, item) for item in v) for k, v in choices_for_widgets.items()}

    def converts_dictionary(self) -> dict:
        """
        Converts dictionary values from a tuple to a list and removes duplication.
        :return: Dictionary. Example {"level_of_care": ["small", "medium", "high"], }
        """
        return {key: [v[0] for v in values] for key, values in self.creates_choices_for_widgets().items()}

    def creates_default_filters_for_start_page(self) -> dict:
        """
        Creates default filters for start page.
        :return: Dictionary. Example {"level_of_care__in": ["small", "medium", "high"], }
        """
        return {f'{k}__in': v for k, v in self.converts_dictionary().items()}

    def changing_value_of_filters(self, request: HttpRequest) -> dict:
        """
        Changing value of filters for page.
        param request: Http Request
        :return: Dictionary. Example {"level_of_care__in": ["small", "medium", "high"], }
        """
        return {f'{k}__in': request.POST.getlist(k) if request.POST.getlist(k) else v for k, v in
                self.converts_dictionary().items()}

    @staticmethod
    def generates_page_by_filters(page_number: HttpResponse, dict_with_filter: dict) -> QuerySet:
        """
        Uses a paginator to split a QuerySet into Page objects.
        param: page_number - Http Response,
        param: dict_with_filter - dict
        :return: Page objects
        """
        obj = HousePlants.objects.filter(**dict_with_filter)
        paginator = Paginator(obj, 30)
        page_obj = paginator.get_page(page_number)

        return page_obj
