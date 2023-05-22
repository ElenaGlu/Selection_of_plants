from django import forms
from .models import HousePlants

class CheckBoxForm(forms.Form):
    unique_level_of_care = []
    list_level_of_care = []
    all_plants = HousePlants.objects.all()
    for plant in all_plants:
        level_of_care = plant.level_of_care
        list_level_of_care.append(level_of_care)
    unique_level_of_care = set(list_level_of_care)
    CHOICES = tuple((item, item) for item in unique_level_of_care if item)

    level_of_care = forms.ChoiceField(label="Сложность ухода", widget=forms.RadioSelect, choices=CHOICES, required=False)
    # light_level = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    # irrigation_level = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    # temperature = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    # humidity = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    # feeding = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
