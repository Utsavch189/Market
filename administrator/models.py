from django.db import models

class ApprovedUsers(models.Model):
    first_name=models.CharField(null=True,blank=True,max_length=500)
    last_name=models.CharField(null=True,blank=True,max_length=500)
    email=models.CharField(null=True,blank=True,max_length=500)
    contact_no=models.CharField(null=True,blank=True,max_length=500)
    whatsapp_no=models.CharField(null=True,blank=True,max_length=500)
    role=models.CharField(null=True,blank=True,max_length=500)

    def __str__(self):
        return self.first_name + ' '+ self.last_name
