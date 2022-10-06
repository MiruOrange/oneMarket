# from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ProductModel(models.Model):
    pname = models.CharField(max_length=30 ,null=False)
    pprice = models.IntegerField(null=False)
    pimage = models.CharField(max_length=40, null=False)
    pdescription = models.TextField(null = False)

class OrderModel(models.Model):
    subtotal = models.IntegerField()
    shipping = models.IntegerField()
    grandtotal = models.IntegerField()
    customername = models.CharField(max_length=50)
    customeremail = models.CharField(max_length=50)
    customeraddress = models.CharField(max_length=50)
    customerphone = models.CharField(max_length=50)
    paytype = models.CharField(max_length=5, default='atm')

class DetailModel(models.Model):
    dorder = models.ForeignKey('OrderModel', on_delete=models.CASCADE)
    pname = models.CharField(max_length=50)
    unitprice = models.IntegerField()
    quantity = models.IntegerField()
    dtotal = models.IntegerField()
    
class User(AbstractUser):#使用django內鍵新增帳號，來增加需要的欄位
    cBirthday = models.DateField(null=True)
    cPhone = models.CharField(max_length=10)

class Visit(models.Model):
    times = models.IntegerField()
    
