from django.contrib import admin
from django.urls import path,include
from blog1 import views
urlpatterns = [
    path("",views.index,name=" ")
    
   
]