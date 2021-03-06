from django.shortcuts import render
from django.views import generic
from .models import Employee

# Create your views here.
class IndexView(generic.ListView):
    # template_name = 'employee/employee_list.html'
    model = Employee