
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('login',views.handlelogin,name='login'),
    path('mountain',views.mountain,name='mountain'),
    path('signup',views.handlesignup,name='signup'),
    path('logout',views.handlelogout,name='logout'),
    path('search',views.handlesearch,name='search'),
    path('formvalidations',views.formvalidations,name='search'),
]

