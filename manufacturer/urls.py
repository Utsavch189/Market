from django.urls import path
from .views import *

urlpatterns = [
    path('production/',index,name='production'),
    path('setproducts/',setproducts,name='setproducts'),
    path('distributorChannel/',distributorChannel,name='distributorChannel'),
    path('distribution/',distribution,name='distribution'),
    path('seeproducts/',setproduct),
    path('manufacturedproducts/',manufacturedproducts),
    path('distribute/',distribute),
    path('distributiondetails/',distributiondetails),
    path('bestproductmanu/',bestproductmanu)
]