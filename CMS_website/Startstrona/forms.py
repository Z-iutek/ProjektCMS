# forms.py w aplikacji Startstrona

from django import forms
from .models import StanStrony

class StanStronyForm(forms.ModelForm):
    class Meta:
        model = StanStrony
        fields = ['kolor_tla', 'tytul_strony']
