from django.contrib import admin
from .models import DistributeToRetailer,Stock,TotalProducts
# Register your models here.
admin.site.register(DistributeToRetailer)
admin.site.register(Stock)
admin.site.register(TotalProducts)