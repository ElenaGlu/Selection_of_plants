from django import forms

from .finder_services import creates_filters


class CheckBoxForm(forms.Form):
    basic_filters_for_start_page = creates_filters()
    level_of_care = forms.MultipleChoiceField(label="Сложность ухода", widget=forms.CheckboxSelectMultiple,
                                              choices=basic_filters_for_start_page['level_of_care'], required=False)
    light_level = forms.MultipleChoiceField(label="Освещенность", widget=forms.CheckboxSelectMultiple,
                                            choices=basic_filters_for_start_page['light_level'],
                                            required=False)
    irrigation_level = forms.MultipleChoiceField(label="Полив", widget=forms.CheckboxSelectMultiple,
                                                 choices=basic_filters_for_start_page['irrigation_level'],
                                                 required=False)
    temperature = forms.MultipleChoiceField(label="Температура содержания", widget=forms.CheckboxSelectMultiple,
                                            choices=basic_filters_for_start_page['temperature'], required=False)
    humidity = forms.MultipleChoiceField(label="Влажность воздуха", widget=forms.CheckboxSelectMultiple,
                                         choices=basic_filters_for_start_page['humidity'],
                                         required=False)
    feeding = forms.MultipleChoiceField(label="Частота удобрения", widget=forms.CheckboxSelectMultiple,
                                        choices=basic_filters_for_start_page['feeding'],
                                        required=False)
