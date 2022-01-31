from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.contrib.auth import get_user_model
# Create your views here.
from django.views.generic import ListView, DetailView


class ProductsList(ListView):
    """
    this is list view for post useing genric list view
    """
    model = Products
    context_object_name = 'products'
    template_name = 'makeup/products.html'
class HomeList(ListView):
    """
    this is list view new products useing genric list view
    """
    model = Products
    # context_object_name = 'products'
    template_name = 'makeup/index.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HomeList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        User = get_user_model()
        myReport={"Products":Products.objects.all().count(),"Brand":Brand.objects.all().count(),"Users":User.objects.all().count()}
        context['reports']=myReport
        context['newest']  = Products.objects.all()
        # context['newest']  = Products.objects.exclude(id=Products.id).distinct().order_by("-expir_date")[:3]
        
        return context
class BrandsList(ListView):
    """
    this is list view for post useing genric list view
    """
    model = Brand
    context_object_name = 'brands'
    template_name = 'makeup/brands.html'
class ProductDetailView(DetailView):
      model = Products
      template_name='makeup/products_details.html'
      context_object_name = 'product'    
def home(request):
    '''
    this is  view to show home page
    '''
    User = get_user_model()
    myReport={"Products":Products.objects.all().count(),"Brand":Brand.objects.all().count(),"Users":User.objects.all().count()}
    # MyModel.objects.order_by('-id')[:1]

    newest=Products.objects.order_by("-id")[:3]
    context={
        'newest' : newest,
        'reports': myReport,
    }
    template_name='makeup/index.html'
    return render(request,template_name,context)

def about(request):
    '''
    this is  view to show about page
    '''
    template_name='makeup/about.html'
    return render(request,template_name)
def contact(request):
    '''
    this is  view to show contact page
    '''
    template_name='makeup/contact.html'
    return render(request,template_name)

def brands_list(request):
    '''
    this is  view to show brand page
    '''
    template_name='makeup/brands.html'
    return render(request,template_name)
def products_list(request):
    '''
    this is  view to show products page
    '''
    template_name='makeup/products.html'
    return render(request,template_name)

def brand_details(request):
    '''
    this is  view to show  details of brand 
    '''
    return HttpResponse("Hello")

# def products_details(request):
#     '''
#     this is  view to show  details of products
#     '''
#     template_name='makeup/products_details.html'
#     return render(request,template_name)

