from django.db import models

# Create your models here.


class TaskDetail(models.Model):
    title = models.CharField(max_length=150)
    is_completed = models.BooleanField(default=False)

