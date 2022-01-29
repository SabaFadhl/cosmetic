from tokenize import Name
from django.db import models
from django.core.validators import MinValueValidator
class Brand(models.Model):
    '''
    this model test brand
    '''
    
    Name=models.CharField(max_length=50)
    Orgin=models.CharField(max_length=50)
    
    def __str__(self) :
        return self.Name

    def get_absolute_url(self):
        return f"/brands/{self.Name}/"
    
    
    
class Products(models.Model):
    '''
    this model test brand
    '''
    Name=models.CharField(max_length=50)
    Kind=models.CharField(max_length=50)
    Descreption=models.TextField()
    Expir_date=models.DateField()
    Price=models.PositiveIntegerField(default=10, validators=[MinValueValidator(5)])
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    
    def __str__(self) :
        return self.Name

    def get_absolute_url(self):
        return f"/products/{self.Name}/"