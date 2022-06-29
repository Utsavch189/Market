from django.urls import path
from .views import *

urlpatterns = [
    path('distribute/',index,name='distribute'),
    path('products/',products,name='products'),
    path('retailerChanel/',retailerChanel,name='retailerChanel'),
    path('manufacturerchanel/',manufacturerchanel,name='manufacturerchanel'),
    path('getproducts/',getproducts),
    path('getretailers/',getretailers),
    path('getmanufacturers/',getmanufacturers),
    path('gettotalproducts/',gettotalproducts),
    path('distributiondetails/',distributiondetails),
    path('bestproductmanu/',bestproductmanu)
]
