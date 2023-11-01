from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Userprofile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    mobile=models.CharField(max_length=12,null=True,blank=True)
    gender=models.CharField(max_length=20,null=True,blank=True)
    fullname=models.CharField(max_length=30,null=True,blank=True)
    password2=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.user.username
    

    

ORDERSTATUS = ((1,"pending"),(2,"solved"),(3,"unsolved"))
class allComplaint(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    status=models.IntegerField(choices=ORDERSTATUS,default=1)
    # TYPE=(('ClassRoom',"ClassRoom"),('Teacher',"Teacher"),('Management',"Management"),('College',"College"),('Other',"Other"))
    
    Subject=models.CharField(max_length=200,blank=False,null=True)
    # user=models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    
    Type_of_complaint=models.CharField(null=True,max_length=200)
    Description=models.TextField(max_length=4000,blank=False,null=True)
    Time = models.DateField(auto_now=True)
   
    


