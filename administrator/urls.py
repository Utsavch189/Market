from django.urls import path
from .views import *

urlpatterns = [
    path('pendings/',index,name='pendings'),
    path('api/',pending),
    path('approve/',approve),
    path('approveusers/',approved,name='approveusers')
]
