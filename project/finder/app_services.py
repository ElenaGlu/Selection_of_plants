from typing import Any

from django.core.paginator import Paginator
from django.db.models.query import QuerySet

from .forms import CheckBoxForm
from .models import Plant


class Filter:
    @staticmethod
    def select_plant(page_number: int, form: CheckBoxForm) -> QuerySet:
        """
         Filter and paginate plant records based on the provided filter form.
        :param page_number: The current page number for pagination.
        :param form: The form containing selected filter options.
        :return: Paginator Page object containing up to 30 filtered plant records.
        """
        obj = Plant.objects.all()
        if form.is_valid():
            for field_name, value in form.cleaned_data.items():
                if value:
                    obj = obj.filter(**{f"{field_name}_id__in": value})
        paginator = Paginator(obj, 30)
        page_obj = paginator.get_page(page_number)
        return page_obj


class ContentPlant:
    @staticmethod
    def process_incorrect_info(pk) -> tuple[Any, dict[Any, Any]]:
        """
        Retrieve a plant by its primary key and prepare its related information for display.
        :param:pk: The primary key of the plant to be displayed.
        :return: A tuple containing:
                - The Plant instance.
                - A dictionary with the plant's related information (e.g., region, soil, flowering time, leaf color).
        """
        field_map = {
            'region': 'name',
            'soil': 'soil',
            'flowering_time': 'time',
            'leaf_color': 'color'
        }
        content = {}
        plant = Plant.objects.get(pk=pk)
        for k, v in field_map.items():
            item = getattr(plant, k)
            content[k] = getattr(item, v)
        return plant, content

