from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class IndexView(generic.TemplateView):
    # template_name = 'blog/post_list.html'
    model = Post