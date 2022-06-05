from django.urls import path
from .views import *

urlpatterns = [
    path('production/',index,name='production'),
]