from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    '''
    this is  view to show home page
    '''
    template_name='index.html'
    return render(request,template_name)
def about(request):
    '''
    this is  view to show about page
    '''
    template_name='about.html'
    return render(request,template_name)
def contact(request):
    '''
    this is  view to show contact page
    '''
    template_name='contact.html'
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
def products_details(request):
    '''
    this is  view to show  details of products
    '''
  
    return HttpResponse("Hello")