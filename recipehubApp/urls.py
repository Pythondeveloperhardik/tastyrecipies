
from django.urls import path
from recipehubApp import views

urlpatterns = [

    path('momo',views.index),
    path('login',views.login),
    path('register',views.register),
    path('recipeinfo',views.recipeinfo)
   
]