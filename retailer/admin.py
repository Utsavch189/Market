from django.contrib import admin
from .models import DistributeToCustomer,RetailerStock,TotalProducts

admin.site.register(RetailerStock)
admin.site.register(DistributeToCustomer)
admin.site.register(TotalProducts)
