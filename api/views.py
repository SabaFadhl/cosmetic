from django.shortcuts import render,HttpResponse
# Create your views here.
from rest_framework import viewsets, generics, mixins
from .serializer import BrandSerializer, ProductsSerializer
from makeup.models import Brand
from django.shortcuts import render
# Create your views here.
from makeup.models import Brand, Products
from .models import favorite
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
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
        """
        this view for git list brands
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        this view for create new brand
        """
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
        """
        this view for retrieve brands
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        this view for update brand of specific id
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        this view for delete brand of specific id
        """
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
        """
        this view for retrieve brand info of  specific id
        data:
        name, orgin
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        this view for update brand with specific id
        data:
        name, orgin
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        this view for delete brand with specific id
        data:
        name, orgin
        """
        return self.destroy(request, *args, **kwargs)


class BrandList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get(self, request, *args, **kwargs):
        """
        this view for retrieve brands
        data:
        name, orgin
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        this view for create new brand
        data:
        name, orgin
        """
        return self.create(request, *args, **kwargs)

class favoriteProductCreate(APIView):
    """
    this view for make like for post
    """
    permission_classes = [IsAuthenticated]


    def get(self, request, **kwargs):
        """
        get request for api
        """
        product_id = None
        product = None


        if request.GET['product_id']:
            product_id = request.GET['product_id']
        # print(post_id)
        try:
            product = Products.objects.get(id=product_id)
            fav = favorite.objects.filter(product=product, user=request.user)
            if fav:
                fav.delete()      
                return Response({'status': False})

        except Products.DoesNotExist:
            return Response({'status': False})

        # print(request.GET)
        if product:
            fav = favorite.objects.create(product=product, user=request.user)

        return Response({'status': True})
    
