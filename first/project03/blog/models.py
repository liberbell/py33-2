from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    # Blog category
    name = models.CharField('category_name', max_length=255)
    created_at = models.DateTimeField('created_date', timezone.now)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    # Blog content
    title = models.CharField('title', max_length=255)
    text = models.TextField('content')
    created_at = models.DateTimeField('created_date', default=timezone.now)