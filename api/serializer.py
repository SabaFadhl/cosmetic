from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
from makeup.models import *
from .models import *


class BrandSerializer(serializers.ModelSerializer):
    """
    this seriliazer for models brand to create, update, delete
    """
    class Meta:
        model = Brand
        # fields = '__all__'
        fields = ['name', 'orgin']

class ProductsSerializer(serializers.ModelSerializer):
    """
    this seriliazer for models Products to create, update, delete
    """
    class Meta:
        model = Products
        # fields = '__all__'
        # fields = ['name', 'kind','price',]
        fields = '__all__'
class FavoriteSerializer(serializers.ModelSerializer):
    """
    this seriliazer for models Products to create, update, delete
    """
    class Meta:
        model = favorite
        # fields = '__all__'
        # fields = ['name', 'kind','price',]
        fields = 'product'