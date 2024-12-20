from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login, logout
from django.contrib import messages


# Create your views here.
def index(request):
   if request.user.is_anonymous:
       return redirect("/login")
   return render(request,'index.html')

def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        #check whether user has entered correct credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
             #A backend authenticated the credentials
             auth_login(request, user)
             return redirect("/")
        else:
            # No backend authenticated the credentials
            messages.error(request, "Invalid username or password")  # Display error message
            return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

