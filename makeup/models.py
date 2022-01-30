from tokenize import Name
from django.db import models
from django.core.validators import MinValueValidator
class Brand(models.Model):
    '''
    this model test brand
    '''
    
    name=models.CharField(max_length=50)
    orgin=models.CharField(max_length=50)
    
    def __str__(self) :
        return self.name

    def get_absolute_url(self):
        return f"/brands/{self.name}/"
    
    
    
class Products(models.Model):
    '''
    this model test brand
    '''
    name=models.CharField(max_length=50)
    kind=models.CharField(max_length=50)
    descreption=models.TextField(null=True)
    expir_date=models.DateField(null=True)
    price=models.PositiveIntegerField(default=10, validators=[MinValueValidator(5)])
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    
    def __str__(self) :
        return self.name

    def get_absolute_url(self):
        return f"/products/{self.name}/"