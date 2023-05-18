from django import forms


class CheckBoxForm(forms.Form):
    CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )

    level_of_care = forms.ChoiceField(label="level_of_care", widget=forms.RadioSelect, choices=CHOICES)
    # light_level = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    # irrigation_level = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    # temperature = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    # humidity = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    # feeding = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
