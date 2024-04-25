from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
import random
from FinalProject import settings
from django.contrib.auth import logout
import requests

# Create your views here.
def index(request):
    return render(request,'index.html')

def signin(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        fnm=usersignup.objects.get(username=unm)
        uid=usersignup.objects.get(username=unm)
        print("Firstname:",fnm.firstname)
        print("UserID:",uid.id)
        user=usersignup.objects.filter(username=unm,password=pas)
        if user:
            print("Login Successfully!")
            #request.session['user']=unm #session create
            request.session['user']=fnm.firstname
            request.session['uid']=uid.id
            #request.session.set_expiry(300)
            return redirect('notes')
        else:
            print("Error!Something went wrong...Try again")
    return render(request,'signin.html')

otp=random.randint(1111,9999)
def signup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")

            #Send OTP on Mobile
            
            url = "https://www.fast2sms.com/dev/bulkV2"
            querystring = {"authorization":"KEodGZf5czOn3eCxJPkWAFHQUYtS86Rbmrv1MyuViag4hs7N2DujvzKSw5MN9mRryb3LC4DsIHiWph78","variables_values":f"{otp}","route":"otp","numbers":"9328480560,7567626592,9016142910,8511583024"}
            headers = {
                'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)


            #Send Email for OTP
           
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
    #user=request.session.get('user')
    user=request.session.get('user')
    if request.method=='POST':
        newnotes=notesForm(request.POST,request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Your notes has been submitted!")
        else:
            print(newnotes.errors)
    return render(request,'notes.html',{'user':user})

def profile(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    cuser=usersignup.objects.get(id=uid)
    if request.method=='POST':
        updateuser=updateForm(request.POST,instance=cuser)
        if updateuser.is_valid():
            updateuser.save()
            print("Your profile has been updated!")
        else:
            print(updateuser.errors)
    return render(request,'profile.html',{'user':user,'cuser':cuser})

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

def userlogout(request):
    logout(request)
    return redirect('/')
