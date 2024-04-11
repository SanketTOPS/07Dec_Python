from django.contrib import admin
from django.urls import path,include
from myapp import views


urlpatterns = [
   path('',views.index),
   path('signin/',views.signin),
   path('signup/',views.signup),
   path('notes/',views.notes),
   path('profile/',views.profile),
   path('about/',views.about),
   path('contact/',views.contact),
]