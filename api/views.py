from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets,generics
from .serializer import BrandSerializer
from makeup.models import Brand
from django.shortcuts import render
# Create your views here.
from makeup.models import Brand
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

# class BrandViewSet(viewsets.ModelViewSet):
#     queryset = Brand.objects.all().order_by('name')
#     serializer_class = BrandSerializer
class BrandApiList(generics.ListCreateAPIView):
    """
    this view for return brand as api list 
    data:
    name, orgin
    """
    queryset = Brand.objects.all().order_by('name')
    serializer_class = BrandSerializer
    permission_classes = [AllowAny]


    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = Post.objects.all()
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(serializer.data)