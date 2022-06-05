from django.urls import path
from .views import *

urlpatterns = [
    path('production/',index,name='production'),
    path('setproducts/',setproducts,name='setproducts'),
    path('distribution/',distribution,name='distribution'),
    path('seeproducts/',setproduct),
    path('manufacturedproducts/',manufacturedproducts),
    path('distribute/',distribute),
]