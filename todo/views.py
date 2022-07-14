from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Todo

# Create your views here.
def index(request):
    # return (HttpResponse('<h1> TODO</h1>') )
    if request.method == 'POST':
        todotask = request.POST['task']

        todo = Todo(task=todotask)
        todo.save()
        messages.info(request, 'Successfully Added')
        return redirect('/')
    
    else:
        alltask = Todo.objects.all()
        return render(request, 'todo/index.html', {'alltasks': alltask})


def deleteTask(request, id):
    if request.method == 'POST':
        task = Todo.objects.get(pk=id)
        task.delete()
        return redirect('/')

def updateTask(request, id):
    # if request.method == 'POST':
    #     task = Todo.objects.get(pk=id)
    # else:
    task = Todo.objects.get(pk=id)
    

    
    return render(request, 'todo/update.html', {'tasks': task} )

    