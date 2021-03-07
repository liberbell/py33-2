from django import forms
from .models import Club, Department

class SearchForm(forms.Form):
    club = 