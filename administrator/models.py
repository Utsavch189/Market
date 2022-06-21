from django.db import models
from django.contrib.auth.models import User
from datetime import date

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
        return self.first_name + ' '+ self.last_name+'('+self.role+')'


class DeletedUser(models.Model):
    first_name=models.CharField(null=True,blank=True,max_length=500)
    last_name=models.CharField(null=True,blank=True,max_length=500)
    email=models.CharField(null=True,blank=True,max_length=500)
    contact_no=models.CharField(null=True,blank=True,max_length=500)
    whatsapp_no=models.CharField(null=True,blank=True,max_length=500)
    role=models.CharField(null=True,blank=True,max_length=500)
    date=models.DateField(date.today(),null=True,blank=True)

    def __str__(self):
        return self.first_name + ' '+ self.last_name+'('+self.role+')'