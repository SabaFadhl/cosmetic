from tokenize import Name
from django.db import models

class Brand(models.Model):
    '''
    this model test brand
    '''
    
    Name=models.CharField(max_length=50)
    Orgin=models.CharField(max_length=50)

class Products(models.Model):
    '''
    this model test brand
    '''
    Name=models.CharField(max_length=50)
    Kind=models.CharField(max_length=50)
    Descreption=models.CharField(max_length=50)
    Expir_date=models.DateField()
    Price=models.IntegerField()
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    
    