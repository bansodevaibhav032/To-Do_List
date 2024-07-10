
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from app.views import home,login,signup,add_todo
 

urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('add-todo/',add_todo,name='add_todo'),
]
