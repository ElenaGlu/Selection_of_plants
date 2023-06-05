from django import forms
from .models import HousePlants


def meth():
    list_item = []
    list_tuple = []
    list_choices = []
    dict_1 = {}
    dict_col = {'level_of_care': [], 'light_level': [], 'irrigation_level': [],
                'temperature': [], 'humidity': [], 'feeding': []}

    all_plants = HousePlants.objects.all()
    for plant in all_plants:
        # list_col = [plant.level_of_care, plant.light_level, plant.irrigation_level,
        #             plant.temperature, plant.humidity, plant.feeding]
        for key in dict_col.keys():
            dict_col[key].append(plant.__dict__[key])

    for key, value in dict_col.items():
        value = set(value)
        dict_1[key] = value
    filtered = {k: v for k, v in dict_1.items() if v is not None}
    return filtered


class CheckBoxForm(forms.Form):
    dict_1 = meth()

    level_of_care = forms.MultipleChoiceField(label="Сложность ухода", widget=forms.CheckboxSelectMultiple,
                                              choices=dict_1['level_of_care'], required=False)
    light_level = forms.MultipleChoiceField(label="Освещенность", widget=forms.CheckboxSelectMultiple,
                                            choices=dict_1['light_level'],
                                            required=False)
    irrigation_level = forms.MultipleChoiceField(label="Полив", widget=forms.CheckboxSelectMultiple,
                                                 choices=dict_1['irrigation_level'],
                                                 required=False)
    temperature = forms.MultipleChoiceField(label="Температура содержания", widget=forms.CheckboxSelectMultiple,
                                            choices=dict_1['temperature'], required=False)
    humidity = forms.MultipleChoiceField(label="Влажность воздуха", widget=forms.CheckboxSelectMultiple,
                                         choices=dict_1['humidity'],
                                         required=False)
    feeding = forms.MultipleChoiceField(label="Частота удобрения", widget=forms.CheckboxSelectMultiple,
                                        choices=dict_1['feeding'],
                                        required=False)
