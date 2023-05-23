from django import forms
from .models import HousePlants


class CheckBoxForm(forms.Form):
    unique_level_of_care = []
    list_level_of_care = []

    unique_light_level = []
    list_light_level = []

    unique_irrigation_level = []
    list_irrigation_level = []

    unique_temperature = []
    list_temperature = []

    unique_humidity = []
    list_humidity = []

    unique_feeding = []
    list_feeding = []

    all_plants = HousePlants.objects.all()
    for plant in all_plants:
        level_of_care = plant.level_of_care
        list_level_of_care.append(level_of_care)

        light_level = plant.light_level
        list_light_level.append(light_level)

        irrigation_level = plant.irrigation_level
        list_irrigation_level.append(irrigation_level)

        temperature = plant.temperature
        list_temperature.append(temperature)

        humidity = plant.humidity
        list_humidity.append(humidity)

        feeding = plant.feeding
        list_feeding.append(feeding)

    unique_level_of_care = set(list_level_of_care)
    CHOICES1 = tuple((item, item) for item in unique_level_of_care if item)

    unique_light_level = set(list_light_level)
    CHOICES2 = tuple((item, item) for item in unique_light_level if item)

    unique_irrigation_level = set(list_irrigation_level)
    CHOICES3 = tuple((item, item) for item in unique_irrigation_level if item)

    unique_temperature = set(list_temperature)
    CHOICES4 = tuple((item, item) for item in unique_temperature if item)

    unique_humidity = set(list_humidity)
    CHOICES5 = tuple((item, item) for item in unique_humidity if item)

    unique_feeding = set(list_feeding)
    CHOICES6 = tuple((item, item) for item in unique_feeding if item)

    level_of_care = forms.MultipleChoiceField(label="Сложность ухода", widget=forms.CheckboxSelectMultiple,
                                              choices=CHOICES1, required=False)
    light_level = forms.MultipleChoiceField(label="Освещенность", widget=forms.CheckboxSelectMultiple, choices=CHOICES2,
                                    required=False)
    irrigation_level = forms.MultipleChoiceField(label="Полив", widget=forms.CheckboxSelectMultiple, choices=CHOICES3,
                                         required=False)
    temperature = forms.MultipleChoiceField(label="Температура содержания", widget=forms.CheckboxSelectMultiple,
                                    choices=CHOICES4, required=False)
    humidity = forms.MultipleChoiceField(label="Влажность воздуха", widget=forms.CheckboxSelectMultiple, choices=CHOICES5,
                                 required=False)
    feeding = forms.MultipleChoiceField(label="Частота удобрения", widget=forms.CheckboxSelectMultiple, choices=CHOICES6,
                                required=False)
