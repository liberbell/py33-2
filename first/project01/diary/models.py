from django.db import models
from django.utils import timezone

# Create your models here.
class Day(models.Model):
    title = models.CharField('Title', max_length=200)
    text = models.TextField('Text')
    date = models.DateTimeField('DATE', default=timezone.now)

    def __str__(self):
        return self.title
    