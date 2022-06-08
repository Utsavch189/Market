from statistics import mode
from django.db import models
from datetime import date



class Stock(models.Model):
    distributor=models.CharField(null=True,blank=True,max_length=1000)
    product_id=models.CharField(null=True,blank=True,max_length=1000)
    product_name=models.CharField(null=True,blank=True,max_length=1000)
    product_price=models.CharField(null=True,blank=True,max_length=1000)
    product_desc=models.CharField(null=True,blank=True,max_length=1000)
    total=models.CharField(null=True,blank=True,max_length=1000)



class DistributeToRetailer(models.Model):
    user=models.CharField(null=True,blank=True,max_length=1000)
    username=models.CharField(null=True,blank=True,max_length=1000)
    product_id=models.CharField(null=True,blank=True,max_length=1000)
    product_name=models.CharField(null=True,blank=True,max_length=1000)
    product_quantity=models.CharField(null=True,blank=True,max_length=1000)
    total_price=models.CharField(null=True,blank=True,max_length=1000)
    distributor_id=models.CharField(null=True,blank=True,max_length=1000)
    date=models.DateField(date.today())



