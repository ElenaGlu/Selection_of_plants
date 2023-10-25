from django import forms

from .finder_services import Filters


class CheckBoxForm(forms.Form):
    choices_for_widgets = Filters.creates_choices_for_widgets()
    level_of_care = forms.MultipleChoiceField(label="Сложность ухода", widget=forms.CheckboxSelectMultiple,
                                              choices=choices_for_widgets['level_of_care'], required=False)
    light_level = forms.MultipleChoiceField(label="Освещенность", widget=forms.CheckboxSelectMultiple,
                                            choices=choices_for_widgets['light_level'],
                                            required=False)
    irrigation_level = forms.MultipleChoiceField(label="Полив", widget=forms.CheckboxSelectMultiple,
                                                 choices=choices_for_widgets['irrigation_level'],
                                                 required=False)
    temperature = forms.MultipleChoiceField(label="Температура содержания", widget=forms.CheckboxSelectMultiple,
                                            choices=choices_for_widgets['temperature'], required=False)
    humidity = forms.MultipleChoiceField(label="Влажность воздуха", widget=forms.CheckboxSelectMultiple,
                                         choices=choices_for_widgets['humidity'],
                                         required=False)
    feeding = forms.MultipleChoiceField(label="Частота удобрения", widget=forms.CheckboxSelectMultiple,
                                        choices=choices_for_widgets['feeding'],
                                        required=False)
