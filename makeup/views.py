from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    '''
    this is  view to show homepage
    '''
  
    return HttpResponse("Hello")
def brand_list(request):
    '''
    this is  view to show brand page
    '''
  
    return HttpResponse("brand_list")
def products_list(request):
    '''
    this is  view to show products page
    '''
  
    return HttpResponse("products_list")
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