from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')    

def recipeinfo(request):
    return render(request,'recipeinfo.html')



