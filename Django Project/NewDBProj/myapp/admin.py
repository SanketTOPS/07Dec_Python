from django.contrib import admin
from .models import *

# Register your models here.
class studData(admin.ModelAdmin):
    list_display=['id','firstname','lastname','email','dob','mobile']

admin.site.register(studinfo,studData)
