from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return (HttpResponse('<h1> TODO</h1>') )
    
    return render(request, 'todo/index.html')