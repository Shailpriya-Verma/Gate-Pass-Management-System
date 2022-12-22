from django.db import models
from datetime import  datetime

class registration(models.Model):
    name=models.CharField(max_length=100)
    rid=models.CharField(max_length=100,primary_key=True)
    passwd=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    address=models.TextField()
    pic=models.ImageField(upload_to="static/Profile/",null=True)
    ryear=models.CharField(max_length=40)
    mob=models.CharField(max_length=60)
    email=models.CharField(max_length=100)


class guardregistration(models.Model):
    name=models.CharField(max_length=100)
    guardid=models.IntegerField(primary_key=True)
    passwd=models.CharField(max_length=100)
    address=models.TextField()
    pic=models.ImageField(upload_to="static/Profile/",null=True)
    mob=models.CharField(max_length=60)
    email=models.CharField(max_length=100)
    rdate=models.DateField()

class adminlogin(models.Model):
    userid=models.CharField(max_length=60,primary_key=True)
    passwd=models.CharField(max_length=100)

class requestpass(models.Model):
    regid=models.IntegerField()
    fromdate=models.DateField()
    fromtime=models.TimeField()
    todate=models.DateField()
    totime=models.TimeField()
    reqtime=models.DateTimeField()
    reason=models.TextField()
    status=models.BooleanField()
    adminremark=models.TextField()
    permittime=models.DateTimeField(null=True, blank=True)
    permitstatus=models.CharField(max_length=100)





