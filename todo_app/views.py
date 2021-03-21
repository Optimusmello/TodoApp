from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

# Create your views here.

@login_required(login_url='signin')
def home(request):

    todo = Todo.objects.filter(user=request.user)
    return render(request,'home.html',{'todo':todo})

def create(request):

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        todo = Todo.objects.create(
            title = title,
            description = description,
            user = request.user
        )
        todo.save()
        return redirect('home')
    return render(request,'create.html')

def delete(request,pk):

    todo = get_object_or_404(Todo,pk=pk)
    if request.method == 'POST':
        Todo.objects.get(pk=pk).delete()
        return redirect('home')
    return render(request,'delete.html',{'todo':todo})

def did_it(request,pk):

    todo = get_object_or_404(Todo,pk=pk)
    if request.method == 'POST':
        todo.completed = True
        todo.save()
        return redirect('home')

    return render(request,'did_it.html',{'todo':todo})
