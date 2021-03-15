from django.shortcuts import render
from django.views import generic
from .models import Post
from django.db.models import Q

# Create your views here.
class IndexView(generic.ListView):
    # template_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        queryset = Post.objects.order_by('-created_at')
        keyword = self.request.GET.get('search-key')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset