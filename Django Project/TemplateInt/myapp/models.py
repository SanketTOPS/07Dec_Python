from django.db import models

# Create your models here.

class contactdata(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    sub=models.CharField(max_length=100)
    msg=models.TextField()

class usersignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    cpassword=models.CharField(max_length=10)

