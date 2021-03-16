from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post, Category, Comment
from django.db.models import Q
from .forms import CommentCreateForm

# Create your views here.
class IndexView(generic.ListView):
    # template_name = 'blog/post_list.html'
    model = Post
    paginate_by = 2

    def get_queryset(self):
        queryset = Post.objects.order_by('-created_at')
        keyword = self.request.GET.get('search-key')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset

class CategoryView(generic.ListView):
    model = Post
    paginate_by = 2

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = Post.objects.order_by('-created_at').filter(category=category)
        return queryset

class DetailView(generic.DetailView):
    model = Post

class CommentView(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        post_pk = self.kwargs['post_pk']
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=post_pk)
        comment.save()
        return redirect('blog:detail', pk=post_pk)