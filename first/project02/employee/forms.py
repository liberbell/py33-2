from django import forms
from .models import Club, Department

class SearchForm(forms.Form):
    club = forms.ModelChoiceField(queryset=Club.objects, label='club_name', required=False)

    department = forms.ModelChoiceField(queryset=Department.objects, label='department_name', required=False)