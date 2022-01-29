from django.urls import path

from . import views

urlpatterns = [
    path('about/',views.about,name="about"),
    # path('products/<int:id>',views.post_details,name="products-details"),
    path('contact/',views.contact,name="contact"),
    path('brands/',views.brands_list,name="brands"),
    path('products/',views.products_list,name="products"),
]