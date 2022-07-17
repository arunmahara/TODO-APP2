from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Todo

# Create your views here.
# function to show and save todo task
def index(request):
    if request.method == 'POST':
        todotask = request.POST['task']

        if todotask : #checks if task-field is empty
            todo = Todo(task=todotask)
            todo.save() #save task
            messages.info(request, 'Successfully Added')
            return redirect('/')
        else:
            messages.info(request, 'Please enter task') #shows this messasge if task-field is empty
            return redirect('/')
    
    else:
        alltask = Todo.objects.all().order_by('-date') #get all todo tasks according to date created created
        return render(request, 'todo/index.html', {'alltasks': alltask})

# function to delete todo task
def deleteTask(request, id):
    if request.method == 'POST':
        task = Todo.objects.get(pk=id)  #get task of requested id
        task.delete()  #delete task of request id
        messages.info(request, 'Successfully Deleted')
        return redirect('/')

# function to update todo task
def updateTask(request, id):
    if request.method == 'POST':
        tasks = Todo.objects.get(pk=id) #get task of requested id
        tasks.task = request.POST['task'] #update task
        status = request.POST.get('status') #get value from status checkbox (on/none)

        if status  == 'on':  #checks if status checkbox is checked or not
            tasks.status = True
        else:
            tasks.status = False
            
        tasks.save() #save updated task
        messages.info(request, 'Successfully Updated')
    else:
        tasks = Todo.objects.get(pk=id) #get task of requested id
    return render(request, 'todo/update.html', {'tasks': tasks} )

    