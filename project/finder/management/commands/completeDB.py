import random as rd

from django.core.management.base import BaseCommand

from finder import models
from finder.forms import filters_form


def complete_db():
    dict_filters = filters_form()
    dict_filters = {key: [v[0] for v in values] for key, values in dict_filters.items()}

    list_update = []

    for item in models.HousePlants.objects.all():
        flag = False
        for key in dict_filters.keys():
            atr = getattr(item, key)
            if atr is None:
                flag = True
                setattr(item, key, rd.choice(dict_filters[key]))
        if flag:
            list_update.append(item)
    models.HousePlants.objects.bulk_update(list_update, [*dict_filters.keys()])


class Command(BaseCommand):
    def handle(self, *args, **options):
        # complete_db()
