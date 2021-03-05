from django.db import models
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name = models.CharField('department_name', max_length=20)
    created_at = models.DateTimeField('registerd_date', default=timezone.now)

    def __str__(self):
        return self.name
    