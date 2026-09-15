from django import forms


class AddPlaceForm(forms.Form):
    PLACE_TYPES = [
        ('cafe/restaurant', 'Cafe / Restaurant'),
        ('park/nature', 'Park / Nature'),
        ('relax', 'Relax'),
        ('culture/museum', 'Culture / Museum'),
        ('recreation/education', 'Recreation / Education'),
    ]

    title = forms.CharField(
        max_length=100,
        required=True,
        label='Name of place',
        widget=forms.TextInput(attrs={
            'placeholder': 'Park Natalka',
            'class': 'form-control',
        })
    )
    place_type = forms.ChoiceField(
        choices=PLACE_TYPES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    location = forms.CharField(
        max_length=150,
        required=False,
        label='Location (not required)',
        widget=forms.TextInput(attrs={
            'placeholder': 'Kyiv, Obolon',
            'class': 'form-control',
        })
    )
    rating = forms.IntegerField(
        max_value=5,
        min_value=1,
        label='Input rating (from 1 to 5). 1 by default',
        widget=forms.NumberInput(attrs={
            'placeholder': "1 - 5",
            'class': 'form-control',
        })
    )
    description = forms.CharField(
        required=True,
        label='Write description to a place',
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': "I like this place cuz I live here",
            'class': 'form-control',
        })
    )
