from pickle import FALSE, TRUE
from django.db import models
from xmlrpc.client import boolean


# Create your models here.

class Todo(models.Model):
    task = models.TextField()
    status = models.BooleanField(default=False) 
    date = models.DateTimeField(auto_now=True)

    # def __str__(self):   # to show task name in admin panel instead of TODO object(1)  # no need of this if class is created in admin.py for showing data in table
    #     return (self.task)    # for id or integer => return str(self.task)

