from django.db import models
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name = models.CharField('department_name', max_length=20)
    created_at = models.DateTimeField('registerd_date', default=timezone.now)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    first_name = models.CharField('first_name', max_length=20)
    last_name = models.CharField('last_name', max_length=20)
    email = models.EmailField('email', blank=True)
    department = models.ForeignKey(Department, verbose_name='department', on_delete=models.PROTECT,)
    created_at = models.DateTimeField('registerd_date', default=timezone.now)