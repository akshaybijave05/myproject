from django.db import models
from django.utils import timezone

class Task(models.Model):
    CATEGORY_CHOICES = (
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Study', 'Study'),
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
