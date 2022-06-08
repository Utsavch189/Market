from django.urls import path
from .views import *

urlpatterns = [
    path('distribute/',index,name='distribute'),
    path('products/',products,name='products'),
    path('getproducts/',getproducts),
    path('getretailers/',getretailers),
    path('gettotalproducts/',gettotalproducts)
]
