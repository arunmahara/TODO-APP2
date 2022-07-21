from django.contrib import admin

from django.contrib import admin
from .models import Todo

# Register your models here.

# admin.site.register(Todo) # doesn't show todos in tabular format in admin panel

@admin.register(Todo) #registering model using decorators
class TodoAdmin(admin.ModelAdmin):  #for showing todos in tabular format in admin panel
    list_display = ('id', 'task', 'status', 'date')

# admin.site.register(Todo, TodoAdmin) #registering model without using decorators