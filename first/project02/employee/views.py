from django.shortcuts import render
from django.views import generic
from .models import Employee
from .forms import SearchForm

# Create your views here.
class IndexView(generic.ListView):
    # template_name = 'employee/employee_list.html'
    model = Employee

    def get_context_data(self):
        context = super().get_context_data()