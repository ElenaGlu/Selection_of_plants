from django import forms

from .models import Care, Light, Irrigation, Temperature, Humidity, Feeding


class CheckBoxForm(forms.Form):

    care = forms.ModelMultipleChoiceField(
        queryset=Care.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Сложность ухода",
        required=False
    )
    light = forms.ModelMultipleChoiceField(
        queryset=Light.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Освещенность",
        required=False
    )
    irrigation = forms.ModelMultipleChoiceField(
        queryset=Irrigation.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Полив",
        required=False
    )
    temperature = forms.ModelMultipleChoiceField(
        queryset=Temperature.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Температура содержания",
        required=False
    )
    humidity = forms.ModelMultipleChoiceField(
        queryset=Humidity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Влажность воздуха",
        required=False
    )
    feeding = forms.ModelMultipleChoiceField(
        queryset=Feeding.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Частота удобрения",
        required=False
    )
