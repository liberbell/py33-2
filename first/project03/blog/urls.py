from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
