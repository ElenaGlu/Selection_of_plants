import random as rd

from django.core.management.base import BaseCommand

from finder import models
from finder.finder_services import Filters


def complete_db() -> None:
    """
    Fills the items with a value of None in the database: HousePlants,
    the random value of the possible values from the dictionary dict_filter.
    """
    dict_filters = Filters()
    choices_for_widgets = dict_filters.creates_choices_for_widgets()
    dictionary_with_filters = dict_filters.converts_dictionary(choices_for_widgets)
    list_update = []
    for item in models.HousePlants.objects.all():
        flag = False
        for key in dictionary_with_filters.keys():
            attribute = getattr(item, key)
            if attribute is None:
                flag = True
                setattr(item, key, rd.choice(dictionary_with_filters[key]))
        if flag:
            list_update.append(item)
    models.HousePlants.objects.bulk_update(list_update, [*dictionary_with_filters.keys()])


class Command(BaseCommand):
    def handle(self, *args, **options):
         # complete_db()
