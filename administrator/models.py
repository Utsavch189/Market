from django.db import models
from django.contrib.auth.models import User


class ApprovedUsers(models.Model):
    author=models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    userid=models.CharField(null=True,blank=True,max_length=500)
    first_name=models.CharField(null=True,blank=True,max_length=500)
    last_name=models.CharField(null=True,blank=True,max_length=500)
    email=models.CharField(null=True,blank=True,max_length=500)
    contact_no=models.CharField(null=True,blank=True,max_length=500)
    whatsapp_no=models.CharField(null=True,blank=True,max_length=500)
    role=models.CharField(null=True,blank=True,max_length=500)

    def __str__(self):
        return self.first_name + ' '+ self.last_name


class SetProduct(models.Model):
    name=models.CharField(null=True,blank=True,max_length=500)
    price=models.CharField(null=True,blank=True,max_length=500)
    description=models.CharField(null=True,blank=True,max_length=1500)

    def __str__(self) :
        return self.name