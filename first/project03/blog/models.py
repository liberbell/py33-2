from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # Blog content
    title = models.CharField('title', max_length=255)
    text = models.TextField('content')
    created_at = models.DateTimeField('created_date', default=timezone.now)
