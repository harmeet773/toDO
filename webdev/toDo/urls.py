from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.signin,name="signin"),
    path('adduser',views.adduser, name="adduser"),
    path('home',views.home, name="home"),
    path('logout',views.signout,name="logout")

]