
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from app.views import home
 

urlpatterns = [
    path('',home)
]
