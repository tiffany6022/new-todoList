from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.TextField(max_length=100)
    detail = models.TextField(max_length=100)
    toggle = models.BooleanField()
