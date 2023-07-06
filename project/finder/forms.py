from django import forms

from .finder_services import creates_filters_for_checkbox_form


class CheckBoxForm(forms.Form):
    filters_for_checkbox_form = creates_filters_for_checkbox_form()
    level_of_care = forms.MultipleChoiceField(label="Сложность ухода", widget=forms.CheckboxSelectMultiple,
                                              choices=filters_for_checkbox_form['level_of_care'], required=False)
    light_level = forms.MultipleChoiceField(label="Освещенность", widget=forms.CheckboxSelectMultiple,
                                            choices=filters_for_checkbox_form['light_level'],
                                            required=False)
    irrigation_level = forms.MultipleChoiceField(label="Полив", widget=forms.CheckboxSelectMultiple,
                                                 choices=filters_for_checkbox_form['irrigation_level'],
                                                 required=False)
    temperature = forms.MultipleChoiceField(label="Температура содержания", widget=forms.CheckboxSelectMultiple,
                                            choices=filters_for_checkbox_form['temperature'], required=False)
    humidity = forms.MultipleChoiceField(label="Влажность воздуха", widget=forms.CheckboxSelectMultiple,
                                         choices=filters_for_checkbox_form['humidity'],
                                         required=False)
    feeding = forms.MultipleChoiceField(label="Частота удобрения", widget=forms.CheckboxSelectMultiple,
                                        choices=filters_for_checkbox_form['feeding'],
                                        required=False)
