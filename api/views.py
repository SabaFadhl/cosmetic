from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets,generics,mixins
from .serializer import BrandSerializer,ProductsSerializer
from makeup.models import Brand
from django.shortcuts import render
# Create your views here.
from makeup.models import Brand,Products
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

# class BrandViewSet(viewsets.ModelViewSet):
#     queryset = Brand.objects.all().order_by('name')
#     serializer_class = BrandSerializer
class ProductsList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
class ProductsDetail(generics.ListCreateAPIView,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                   ):
    """
    this view for return Products as api list 
    data:
    name, orgin
    """
    queryset = Products.objects.all().order_by('name')
    serializer_class = ProductsSerializer
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class BrandDetail(generics.ListCreateAPIView,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                   ):
    """
    this view for return brand as api list 
    data:
    name, orgin
    """
    queryset = Brand.objects.all().order_by('name')
    serializer_class = BrandSerializer
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class BrandList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)