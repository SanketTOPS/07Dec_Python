from django.shortcuts import render,redirect
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

def showdata(request):
    stdata=studinfo.objects.all()
    return render(request,'showdata.html',{'stdata':stdata})

def deletedata(request,id):
    stid=studinfo.objects.get(id=id)
    studinfo.delete(stid)
    return redirect('showdata')

