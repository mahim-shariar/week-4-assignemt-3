from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=200)
    task_Description = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField()
    category = models.ManyToManyField(Category)


    def __str__(self):
        return self.task_title