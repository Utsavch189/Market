from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('register/',register),
    path('login/',loginn,name='login'),
    path('logout/',logoutt),
    path('recover/',recover,name='recover'),
    path('manufact/',manufact),
    path('distribut/',distribut),
    path('retailer/',retailer)
]
