from django.contrib import admin

from .models import *
# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'price', 'brand')
    read_only = ('expir_date')
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'orgin')

admin.site.register(Products,ProductsAdmin)
admin.site.register(Brand,BrandAdmin)

