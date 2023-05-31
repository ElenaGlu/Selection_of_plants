from django import forms
from .models import HousePlants


class CheckBoxForm(forms.Form):

    list_item = []
    list_tuple = []
    list_choices = []

    all_plants = HousePlants.objects.all()
    for plant in all_plants:
        list_col = [plant.level_of_care, plant.light_level, plant.irrigation_level,
                    plant.temperature, plant.humidity, plant.feeding]
        for elem in list_col:
            item = elem
            list_item.append(item)

        unique_item = set(list_item)
        choice = tuple((i, i) for i in unique_item if i)
        list_choices.append(choice)

    level_of_care = forms.MultipleChoiceField(label="Сложность ухода", widget=forms.CheckboxSelectMultiple,
                                              choices=list_choices[0], required=False)
    light_level = forms.MultipleChoiceField(label="Освещенность", widget=forms.CheckboxSelectMultiple,
                                            choices=list_choices[1],
                                    required=False)
    irrigation_level = forms.MultipleChoiceField(label="Полив", widget=forms.CheckboxSelectMultiple,
                                                 choices=list_choices[2],
                                         required=False)
    temperature = forms.MultipleChoiceField(label="Температура содержания", widget=forms.CheckboxSelectMultiple,
                                    choices=list_choices[3], required=False)
    humidity = forms.MultipleChoiceField(label="Влажность воздуха", widget=forms.CheckboxSelectMultiple,
                                         choices=list_choices[4],
                                 required=False)
    feeding = forms.MultipleChoiceField(label="Частота удобрения", widget=forms.CheckboxSelectMultiple,
                                        choices=list_choices[5],
                                required=False)
