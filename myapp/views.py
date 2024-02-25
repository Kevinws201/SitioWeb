from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request,"about.html")

def Home(request):
    return render(request,'index.html')

def Login(request):
    return render(request,'login.html')

def Password(request):
    return render(request,'password.html')

def newAccount(request):
    return render(request, 'new.html'),

def mainMenu(request):
    return render(request, 'mainMenu.html')
