from tkinter import CASCADE
from django.db import models
from datetime import date
# Create your models here.

class SetProduct(models.Model):
    name=models.CharField(null=True,blank=True,max_length=500)
    price=models.CharField(null=True,blank=True,max_length=500)
    description=models.CharField(null=True,blank=True,max_length=5000)

    def __str__(self):
        return self.name



class CreatedProducts(models.Model):
    author=models.ForeignKey(SetProduct,on_delete=models.CASCADE,null=True,blank=True)
    Product_id=models.CharField(null=True,blank=True,max_length=500)
    name=models.CharField(null=True,blank=True,max_length=500)
    price=models.CharField(null=True,blank=True,max_length=500)
    description=models.CharField(null=True,blank=True,max_length=1500)
    production_no=models.CharField(null=True,blank=True,max_length=150000000000000)
    production_date=models.DateField(date.today())

    def __str__(self):
        return self.name