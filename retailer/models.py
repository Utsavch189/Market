from django.db import models
from datetime import date

class RetailerStock(models.Model):
    retailer=models.CharField(null=True,blank=True,max_length=1000)
    product_id=models.CharField(null=True,blank=True,max_length=1000)
    product_name=models.CharField(null=True,blank=True,max_length=1000)
    product_price=models.CharField(null=True,blank=True,max_length=1000)
    product_desc=models.CharField(null=True,blank=True,max_length=1000)
    total=models.CharField(null=True,blank=True,max_length=1000)
    def __str__(self):
        return self.product_name


class DistributeToCustomer(models.Model):
    Retailer_id=models.CharField(null=True,blank=True,max_length=1000)
    Retailer_username=models.CharField(null=True,blank=True,max_length=1000)
    product_id=models.CharField(null=True,blank=True,max_length=1000)
    product_name=models.CharField(null=True,blank=True,max_length=1000)
    product_quantity=models.CharField(null=True,blank=True,max_length=1000)
    total_price=models.CharField(null=True,blank=True,max_length=1000)
    date=models.DateField(date.today())
    def __str__(self):
        return self.product_name+'BY :'+' '+self.Retailer_username