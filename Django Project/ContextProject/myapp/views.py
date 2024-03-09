from django.shortcuts import render

# Create your views here.
num=1
def index(request):
    name="Hitesh"
    global num
    num+=1
    return render(request,'index.html',{'nm':name,'num':num})