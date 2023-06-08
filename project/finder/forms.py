from django import forms

from .models import HousePlants


def filters_form() -> dict:
    """
    Collecting unique values in the dictionary for CheckBoxForm and further filtering.
    :return: Dictionary with unique values in the form of a tuple.
    """
    dict_filters = {'level_of_care': [], 'light_level': [], 'irrigation_level': [],
                    'temperature': [], 'humidity': [], 'feeding': []}
    for elem in HousePlants.objects.all():
        for key in dict_filters.keys():
            dict_filters[key].append(elem.__dict__[key])
    for key, value in dict_filters.items():
        filter_value = set(value)
        choices_value = tuple((item, item) for item in filter_value)
        dict_filters[key] = choices_value
    return dict_filters


class CheckBoxForm(forms.Form):
    dict_filters = filters_form()
    level_of_care = forms.MultipleChoiceField(label="Сложность ухода", widget=forms.CheckboxSelectMultiple,
                                              choices=dict_filters['level_of_care'], required=False)
    light_level = forms.MultipleChoiceField(label="Освещенность", widget=forms.CheckboxSelectMultiple,
                                            choices=dict_filters['light_level'],
                                            required=False)
    irrigation_level = forms.MultipleChoiceField(label="Полив", widget=forms.CheckboxSelectMultiple,
                                                 choices=dict_filters['irrigation_level'],
                                                 required=False)
    temperature = forms.MultipleChoiceField(label="Температура содержания", widget=forms.CheckboxSelectMultiple,
                                            choices=dict_filters['temperature'], required=False)
    humidity = forms.MultipleChoiceField(label="Влажность воздуха", widget=forms.CheckboxSelectMultiple,
                                         choices=dict_filters['humidity'],
                                         required=False)
    feeding = forms.MultipleChoiceField(label="Частота удобрения", widget=forms.CheckboxSelectMultiple,
                                        choices=dict_filters['feeding'],
                                        required=False)
