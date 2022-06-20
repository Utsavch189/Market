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
    def __str__(self):
        return self.product_name


class DistributeToRetailer(models.Model):
    Retailer_id=models.CharField(null=True,blank=True,max_length=1000)
    Retailer_username=models.CharField(null=True,blank=True,max_length=1000)
    product_id=models.CharField(null=True,blank=True,max_length=1000)
    product_name=models.CharField(null=True,blank=True,max_length=1000)
    product_quantity=models.CharField(null=True,blank=True,max_length=1000)
    total_price=models.CharField(null=True,blank=True,max_length=1000)
    distributor_id=models.CharField(null=True,blank=True,max_length=1000)
    calculation_status=models.BooleanField(default=False)
    date=models.DateField(date.today())
    def __str__(self):
        return self.Retailer_username+' '+'('+self.product_name+')'+' '+'(from:'+self.distributor_id+')'



