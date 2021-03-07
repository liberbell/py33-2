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
        context['form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        form.is_valid()
        
        # get all employee
        queryset = super().get_queryset()

        # filter by department
        department = form.cleaned_data['department']
        if department:
            queryset = queryset.filter(department=department)