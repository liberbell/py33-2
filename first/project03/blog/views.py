from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class IndexView(generic.ListView):
    # template_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        queryset = Post.objects.order_by('-created_at')
        keyword = self.request.GET.get('search-key')
        if keyword:
            queryset = queryset.filter(title__icontains=keyword)
        return queryset