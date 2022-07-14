from django.db import models

# Create your models here.

class Todo(models.Model):
    text = models.TextField()

