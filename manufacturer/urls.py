from django.urls import path
from .views import *

urlpatterns = [
    path('production/',index,name='production'),
     path('setproducts/',setproducts,name='setproducts'),
    path('seeproducts/',setproduct),
    path('manufacturedproducts/',manufacturedproducts),
]