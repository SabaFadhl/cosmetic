from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from makeup.models import *


class BrandSerializer(serializers.ModelSerializer):
    """
    this seriliazer for models brand to create, update, delete
    """
    class Meta:
        model = Brand
        # fields = '__all__'
        fields = ['name', 'orgin']

