from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    # Blog category
    name = models.CharField('category_name', max_length=255)
    created_at = models.DateTimeField('created_date', default=timezone.now)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    # Blog content
    title = models.CharField('title', max_length=255)
    text = models.TextField('content')
    created_at = models.DateTimeField('created_date', default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    # Blog comment
    name = models.CharField('name', max_length=30, default='nemo')
    text = models.TextField('text')
    post = models.ForeignKey(Post, verbose_name='linkedcontent', on_delete=models.PROTECT)
    created_at = models.DateTimeField('created_date', default=timezone.now)