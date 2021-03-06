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
    
def signin(request):
    if request.method !="POST":
        return render(request,"toDo/signin.html")
        # return HttpResponse("hkjhhh")
    else:
        try:
            name = request.POST.get("name") 
            password = request.POST.get("pwd")             
            usera = authenticate(request,username=name, password=password)
            if usera is not None:
                login(request,usera)
                request.session["name"]=name
                return HttpResponseRedirect(reverse("home") )
            else :
                return  HttpResponseRedirect(reverse("adduser"))           
        except Exception as e :
            print(e) 

def adduser(request):
    
    if request.method != "POST":
        return render(request,"toDo/signup.html")
    else:
        email = request.POST["email"] 
        print("request is                 " , request , email)
        try:
            email = request.POST.get("email") 
            name = request.POST.get("username") 
            password = request.POST.get("pwd") 
            # u = User(name=name,username=username,password=password)
            # u.save()
            print(email,name,password)
            user = User.objects.create_user(name, email, password)
            user.save()
            usera = authenticate(request,username=name, password=password)
            if usera is not None:
                login(request,user)
                request.session['name'] = name
                return HttpResponseRedirect(reverse("home") )
            else :
                return  HttpResponse("error occured")
        
        except Exception as e :
            print(e)
 
def signout(request):
    logout(request)
    request.session['name']= None
    return HttpResponseRedirect(reverse("signin"))

def home(request):
    if request.user.is_authenticated :

        user_name = request.session['name']
        u = User.objects.get(username=user_name)
        if request.method == "POST":
            task = request.POST.get('task')
            print("task is ", task)
            s = Task(created_by=u,task=task)
            s.save()

        tasks_of_user = u.tasks.all()

        return  render(request,"toDo/home.html",{
            "user":user_name,
            "tasks":tasks_of_user
        })