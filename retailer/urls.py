from django.urls import path
from .views import *

urlpatterns = [
    
    path('stock/',stock,name='stock'),
    path('sell/',sell,name='sell'),
    path('gettotalproducts/',gettotalproducts),
    path('distributiondetails/',distributiondetails),
    path('getproducts/',getproducts),
    path('statics/',statics),
    path('bestproductmanu/',bestproductmanu)
]
