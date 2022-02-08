from urllib import request
from django.shortcuts import render, redirect
import requests
from api.models import favorite
from .models import *
from django.http import HttpResponse
from django.contrib.auth import get_user_model
# Create your views here.
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .forms import ProductsForm, NewUserForm
from django.shortcuts import reverse
from django.urls import reverse_lazy
# from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.contrib.auth.decorators import login_required
# from bootstrap_datepicker_plus import DatePickerInput
# from django.contrib.auth import group_required
# @group_required('seller')
from django.contrib.auth.mixins import LoginRequiredMixin
# @login_required

# class SellerProducts(LoginRequiredMixin, ListView):
#     """
#     this is list view for my favorite
#     """
#     model = '/api/favorite-list/'
    
#     context_object_name = 'products'
#     template_name = 'seller/products.html'
def myFavorite(request):
    # response=requests.get('http://127.0.0.1:8000/api/favorite-list').json()
    # print("========response=========")
    # print (response)
    # MyModel.objects.order_by('-id')[:1]

    products=favorite.objects.filter(user=request.user)
    # print(p)
    # products=Products(p.values('product'))
    print("===============")
    
    # print(products)
    print ("]]]]]]]]]]]]",products)
    context = {
        'fav': products,
    }
    template_name = 'makeup/favorite.html'
    return render(request,template_name,context) 
  
class SellerProducts(LoginRequiredMixin, ListView):
    """
    this is list view for products useing genric list view
    """
    model = Products
    context_object_name = 'products'
    template_name = 'seller/products.html'
    queryset = Products.objects.order_by("-id")


class ProductsList(ListView):
    """
    this is list view for post useing genric list view
    """
    model = Products
    context_object_name = 'products'
    template_name = 'makeup/products.html'
    # self.user

    def get(self, request, *args, **kwargs):
        self.user = request.user
        self.request=request
        return super(ProductsList, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductsList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # fav=favorite.objects.filter(user=self.user )
        # fav=favorite.objects.values('product',user=self.user)
        # context['fav'] = fav
        if not self.request.user.is_anonymous :
            print("[[[[[[[[[[[[[[[[[[",self.request.user)
            products_fav = favorite.objects.values_list('product', flat=True).filter(user=self.user)
            fav = Products.objects.filter(pk__in=set(products_fav))
            # print("===========================")
            # print(fav)
            context['fav'] = fav
            return context
        
        context['products'] = Products.objects.all()
        return context
        
        # return 
# class HomeList(ListView):
#     """
#     this is list view new products useing genric list view
#     """
#     model = Products
#     # context_object_name = 'products'
#     template_name = 'makeup/index.html'
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(HomeList, self).get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         User = get_user_model()
#         myReport={"Products":Products.objects.all().count(),"Brand":Brand.objects.all().count(),"Users":User.objects.all().count()}
#         context['reports']=myReport
#         context['newest']  = Products.objects.all()
#         # context['newest']  = Products.objects.exclude(id=Products.id).distinct().order_by("-expir_date")[:3]

#         return context


class BrandsList(ListView):
    """
    this is list view for post useing genric list view
    """
    model = Brand
    context_object_name = 'brands'
    template_name = 'makeup/brands.html'


class ProductDetailView(DetailView):
    model = Products
    template_name = 'makeup/products_details.html'
    context_object_name = 'product'


def home(request):
    '''
    this is  view to show home page
    '''
    User = get_user_model()
    myReport = {"Products": Products.objects.all().count(
    ), "Brand": Brand.objects.all().count(), "Users": User.objects.all().count()}
    # MyModel.objects.order_by('-id')[:1]

    newest = Products.objects.order_by("-id")[:3]
    context = {
        'newest': newest,
        'reports': myReport,
    }
    template_name = 'makeup/index.html'
    return render(request, template_name, context)


def about(request):
    '''
    this is  view to show about page
    '''
    template_name = 'makeup/about.html'
    return render(request, template_name)


def contact(request):
    '''
    this is  view to show contact page
    '''
    template_name = 'makeup/contact.html'
    return render(request, template_name)


def brands_list(request):
    '''
    this is  view to show brand page
    '''
    template_name = 'makeup/brands.html'
    return render(request, template_name)


def products_list(request):
    '''
    this is  view to show products page
    '''
    template_name = 'makeup/products.html'
    return render(request, template_name)


def AddProduct(request, id=None):
    form = ProductsForm

    template_name = 'seller/form.html'

    product = None
    if id:
        try:

            product = Products.objects.get(id=id)
        except Products.DoesNotExist:
            # return redirect('', permanent=False)
            pass
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        print("post")
        if form.is_valid():
            print("valid")

            if not id:
                print("save")

                form.save()
            else:
                form.update(product)
            # return redirect('')
        print(form.errors)
        print(request.POST)
        context = {
            'form': form
        }

        # return redirect('products-seller', permanent=False)
        # return render(request, template_name, context)

    context = {
        'form': ProductsForm()
    }
    if id:
        context = {
            'form': ProductsForm({"name": product.name, "kind": product.kind, "descreption": product.descreption, "expir_date": product.expir_date, "price": product.price, "brand": product.brand})
        }
    return render(request, template_name, context)

# @login_required


class AddProductFormView(FormView):
    template_name = 'seller/form.html'
    form_class = ProductsForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

# @login_required


class productCreateView(CreateView):
    template_name = 'seller/form.html'
    model = Products
    # success_url = 'products-seller'
    fields = ['name', 'kind', 'descreption',
              'expir_date', 'price', 'image', 'brand']
    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['expir_date'].widget = DatePickerInput()
    #     return form

    def get_success_url(self):
        return self.request.GET.get('next', reverse('products-seller'))

# @login_required


class productUpdateView(UpdateView):
    model = Products
    template_name = 'seller/form.html'

    fields = ['name', 'kind', 'descreption', 'expir_date', 'price', 'brand']
    success_url = reverse_lazy('products-seller')

# @login_required


class productDeleteView(DeleteView):
    model = Products
    template_name = 'seller/confirm.html'

    success_url = reverse_lazy('products-seller')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")

    form = NewUserForm()
    return render(request=request, template_name="makeup/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="makeup/login.html", context={"login_form": form})


@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")
