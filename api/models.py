from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=50, blank=False,)
    is_finished = models.BooleanField(default=False, blank=False)