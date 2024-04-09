from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   
   path('',views.index),
   path('about/',views.about),
   path('contact/',views.contact),
   path('faq/',views.faq),
   path('productdetail/',views.productdetail),
   path('products/',views.products),
   path('signin/',views.signin,name='signin'),
   path('signup/',views.signup),
]