from django.urls import path

from . import views
from makeup.views import ProductsList,BrandsList,ProductDetailView,SellerProducts,productUpdateView,productCreateView,productDeleteView

urlpatterns = [
    path('about/',views.about,name="about"),
    # path('products/<int:id>',views.post_details,name="products-details"),
    path('contact/',views.contact,name="contact"),
    path('details/<pk>',ProductDetailView.as_view(),name="product-detail"),
    path('brands/',BrandsList.as_view(),name="brands"),
    path('products/',ProductsList.as_view(),name="products"),
    path('seller/products/',SellerProducts.as_view(),name="products-seller"),
    path('seller/products/add', productCreateView.as_view(), name='add-products'),
    path('seller/products/edit/<int:pk>',productUpdateView.as_view(),name="edit-product"),
    path('seller/products/delete/<int:pk>',productDeleteView.as_view(),name="delete-product"),
    path("accounts/register", views.register_request, name="register"),
    path("accounts/login/", views.login_request, name="login"),
    path("accounts/logout", views.logout_request, name= "logout"),
    
]