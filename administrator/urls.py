from django.urls import path
from .views import *

urlpatterns = [
    path('pendings/',index,name='index'),
    path('api/',pending),
]
