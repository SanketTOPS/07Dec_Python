from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
import random
from FinalProject import settings

# Create your views here.
def index(request):
    return render(request,'index.html')

def signin(request):
    return render(request,'signin.html')


def signup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")

            #Send Email for OTP
            global otp
            otp=random.randint(1111,9999)
            sub="OTP Verification for New user!"
            msg=f"Dear User!\n\nThanks for registraion with us!\nYour one time password is {otp}\n\nThanks & Regards!\nNotesApp Team - Rajkot\n+91 97247 99469 | www.tops-int.com"
            from_email=settings.EMAIL_HOST_USER
            to_email=[request.POST['username']]
            send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=to_email)
            print("Your OTP:",otp)
            return redirect('otpverify')
        else:
            print(newuser.errors)
    return render(request,'signup.html')

def notes(request):
    return render(request,'notes.html')

def profile(request):
    return render(request,'profile.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def otpverify(request):
    global otp
    msg=""
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            return redirect('signin')
        else:
            print("OTP Faild...")
            msg="OTP Faild...Plz enter valid OTP"
    return render(request,'otpverify.html',{'msg':msg})