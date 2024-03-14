from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def index(request):
    msg=""
    if request.method=='POST':
        stdata=studForm(request.POST)
        if stdata.is_valid(): #TRUE
            stdata.save()
            print("Your record has been inserted!")
            msg="Your record has been inserted!"
        else:
            print(stdata.errors)
            msg="Error!Something went wrong....Try again"
    return render(request,'index.html',{'msg':msg})

def showdata(request):
    stdata=studinfo.objects.all()
    return render(request,'showdata.html',{'stdata':stdata})

def updatedata(request):
    return render(request,'updatedata.html')