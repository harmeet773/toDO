# https://docs.djangoproject.com/en/3.1/topics/auth/default/
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse ,HttpResponseRedirect 
# from .forms import Add_User_form , Add_Task_form
from .models import *
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    render(request,)
    


def adduser(request):
    if request.method != "POST":
        return render(request,"toDo/signup.html")
    else:

        try:
            email = request.POST.get("email") 
            name = request.POST.get("name") 
            password = request.POST.get("pwd") 
            # u = User(name=name,username=username,password=password)
            # u.save()
            user = User.objects.create_user(name, email, password)
            user.save()
            usera = authenticate(request,username=name, password=password)
            if usera is not None:
                login(request,user)
            else:
                return HttpResponseRedirect(reverse("index"))
        
        except Exception as e :
            print(e)
