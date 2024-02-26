from django import forms
from .models import CountryPopulation


class CountryPopulationForm(forms.ModelForm):
    class Meta:
        model = CountryPopulation
        fields = '__all__'