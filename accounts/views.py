from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import *
# Create your views here.


def signup(request):

    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            auth_login(request,user)
            return redirect('home')

    return render(request,'signup.html',{'form':form})

def signout(request):

    auth_logout(request)
    return redirect('home')