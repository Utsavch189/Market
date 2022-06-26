from tkinter import CASCADE
from django.db import models
from datetime import date




# Create your models here.

class SetProduct(models.Model):
    manufacturer_id=models.CharField(null=True,blank=True,max_length=500)
    name=models.CharField(null=True,blank=True,max_length=500)
    price=models.CharField(null=True,blank=True,max_length=500)
    description=models.CharField(null=True,blank=True,max_length=5000)

    def __str__(self):
        return self.name+' '+'(BY:'+self.manufacturer_id+')'



class CreatedProducts(models.Model):
    manufacturer_id=models.CharField(null=True,blank=True,max_length=500)
    Product_id=models.CharField(null=True,blank=True,max_length=500)
    name=models.CharField(null=True,blank=True,max_length=500)
    price=models.CharField(null=True,blank=True,max_length=500)
    description=models.CharField(null=True,blank=True,max_length=1500)
    production_no=models.CharField(null=True,blank=True,max_length=150000000000000)
    production_date=models.DateField(date.today())

    def __str__(self):
        return self.name+' '+'(BY:'+self.manufacturer_id+')'


class Distribute(models.Model):
    user=models.CharField(null=True,blank=True,max_length=500)
    username=models.CharField(null=True,blank=True,max_length=500)
    product_id=models.CharField(null=True,blank=True,max_length=500)
    manufacturer_id=models.CharField(null=True,blank=True,max_length=500)
    product_name=models.CharField(null=True,blank=True,max_length=500)
    product_quantity=models.CharField(null=True,blank=True,max_length=500)
    total_price=models.CharField(null=True,blank=True,max_length=500)
    calculation_status=models.BooleanField(default=False)
    date=models.DateField(date.today())

    def __str__(self):
        return self.user + ' '+'('+self.product_name+')'+' '+'( from:'+self.manufacturer_id+')'


class TotalProducts(models.Model):
    product_id=models.CharField(null=True,blank=True,max_length=500)
    manufacturer_id=models.CharField(null=True,blank=True,max_length=500)
    product_name=models.CharField(null=True,blank=True,max_length=500)
    product_quantity=models.CharField(null=True,blank=True,max_length=500)
    date=models.DateField(date.today())
    
    def __str__(self) -> str:
        return self.product_name