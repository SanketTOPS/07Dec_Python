from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    msg=""
    if request.method=='POST':
        newst=studform(request.POST)
        if newst.is_valid():
            newst.save()
            print("Record Inserted!")
            msg="Record Inserted!"
        else:
            print(newst.errors)
            msg="Error!Something went wrong..."
    return render(request,'index.html',{'msg':msg})