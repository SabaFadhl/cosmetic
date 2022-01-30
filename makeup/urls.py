from django.urls import path

from . import views
from makeup.views import ProductsList,BrandsList,ProductDetailView

urlpatterns = [
    path('about/',views.about,name="about"),
    # path('products/<int:id>',views.post_details,name="products-details"),
    path('contact/',views.contact,name="contact"),
    path('details/<pk>',ProductDetailView.as_view(),name="product-detail"),
    path('brands/',BrandsList.as_view(),name="brands"),
    path('products/',ProductsList.as_view(),name="products"),
]