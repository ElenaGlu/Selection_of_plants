from django import forms

from .finder_services import creates_filters_for_form_checkbox


class CheckBoxForm(forms.Form):
    filters_for_forms = creates_filters_for_form_checkbox()
    level_of_care = forms.MultipleChoiceField(label="Сложность ухода", widget=forms.CheckboxSelectMultiple,
                                              choices=filters_for_forms['level_of_care'], required=False)
    light_level = forms.MultipleChoiceField(label="Освещенность", widget=forms.CheckboxSelectMultiple,
                                            choices=filters_for_forms['light_level'],
                                            required=False)
    irrigation_level = forms.MultipleChoiceField(label="Полив", widget=forms.CheckboxSelectMultiple,
                                                 choices=filters_for_forms['irrigation_level'],
                                                 required=False)
    temperature = forms.MultipleChoiceField(label="Температура содержания", widget=forms.CheckboxSelectMultiple,
                                            choices=filters_for_forms['temperature'], required=False)
    humidity = forms.MultipleChoiceField(label="Влажность воздуха", widget=forms.CheckboxSelectMultiple,
                                         choices=filters_for_forms['humidity'],
                                         required=False)
    feeding = forms.MultipleChoiceField(label="Частота удобрения", widget=forms.CheckboxSelectMultiple,
                                        choices=filters_for_forms['feeding'],
                                        required=False)
