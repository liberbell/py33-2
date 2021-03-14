from .models import Category

def Common(request):
    context = {
        'category_list': Category.objects.all(), 
    }
    return context