from pickle import FALSE, TRUE
from django.db import models
from xmlrpc.client import boolean


# Create your models here.

class Todo(models.Model):
    task = models.TextField()
    status = models.BooleanField(default=False) 
    date = models.DateTimeField(auto_now=True)
