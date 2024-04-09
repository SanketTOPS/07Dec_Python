from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    msg=""
    if request.method=='POST':
        newcontact=contactForm(request.POST)
        if newcontact.is_valid():
            newcontact.save()
            print("Your data has been submitted!")
            msg="Your data has been submitted!"

            #Email Send
            send_mail(subject='Thank You!',message=f"Dear User\n\nYour data has been submitted!\n\nEnjoy our services.\n\nThanks & Regards!\nSanket Chauhan | +91 9724799469",from_email='19febdm@gmail.com',recipient_list=['dhruviradadiya81@gmail.com','riktajadav@gmail.com','makwana0843@gmail.com'])

        else:
            print(newcontact.errors)
    return render(request,'contact.html',{'msg':msg})

def faq(request):
    return render(request,'faq.html')

def productdetail(request):
    return render(request,'productdetail.html')

def products(request):
    return render(request,'products.html')

def signin(request):
    if request.method=='POST':

        email=request.POST['email']
        pas=request.POST['password']

        user=usersignup.objects.filter(email=email,password=pas)
        if user:
            print("Login Successfull!")
            return redirect('/')
        else:
            print("Error!Login Faild....")
    return render(request,'signin.html')

def signup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():

            if request.POST['password']==request.POST['cpassword']:
                newuser.save()
                print("Signup Successfully!")
                return redirect('signin')
            else:
                print("Password and Confirm Password does't match....!")
        else:
            print(newuser.errors)
    return render(request,'signup.html')
