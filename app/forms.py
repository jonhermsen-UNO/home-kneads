from django import forms

from .models import Animal, Species


class AdoptForm(forms.ModelForm):
    class Meta:
        model = Animal
        # Order here determines order on the web form.
        fields = [
            'name',
            'is_male',
            'species',
            'weight',
            'birth_date',
            'adoption_fee',
            'image',
        ]

    # Override the default behavior for fields that need special handling.
    species = forms.ModelChoiceField(
        queryset = Species.objects.all(),
        label = 'Species',
        widget = forms.RadioSelect(),
    )
    birth_date = forms.DateField(
        help_text = 'Use a best estimate if the actual date is unknown.',
        widget = forms.TextInput(attrs={'type': 'date'}),
    )
    is_male = forms.ChoiceField(
        label = 'Gender',
        choices = [(True, 'Male'), (False,'Female')],
        widget = forms.RadioSelect(),
    )
