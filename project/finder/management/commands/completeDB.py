from random import *

from finder import models
from .models import HousePlants
from .forms import filters_form

dict_filters = filters_form()
dict_filters = {key: [v[0] for v in values] for key, values in dict_filters.items()}

list_update = []

for item in models.HousePlants.objects.all():
    flag = False
    for key in dict_filters.keys():
        atr = getattr(item, key)
        if item.atr is None:
            item.atr = random.choice(dict_filters[key])
            flag = True
    if True:
        list_update.append(item)
models.HousePlants.objects.bulk_update(list_update, [*dict_filters.keys()])