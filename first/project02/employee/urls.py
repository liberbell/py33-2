from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('', views.IndexViews.as_view(), name='index'),
]
