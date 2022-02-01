from logging import PlaceHolder
from django import forms
from django.core.validators import MinValueValidator

from .models import Products
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class ProductsForm(forms.Form):

    name=forms.CharField(label='name',max_length=50)
    kind=forms.CharField(label='kind',max_length=50)
    descreption=forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    expir_date=forms.DateField(label='expir_date')
    # expir_date=forms.DateField(label='expir_date',widget=forms.TextInput(attrs=
    #                             {
    #                                 'class':'datepicker'
    #                             }))
    price=forms.IntegerField(label='price')
    brand=forms.IntegerField(label='brand')
    
    def save(self, id=None):
        """
        this function for save to model Products
        """
        # if not id:
        name = self.cleaned_data['name']
        kind = self.cleaned_data['kind']
        descreption = self.cleaned_data['descreption']
        expir_date = self.cleaned_data['expir_date']
        price = self.cleaned_data['price']
        brand = self.cleaned_data['brand']

        #rint("this is print of save method", title, text, pub_date)
        return Products.objects.create(name=name,kind=kind,descreption=descreption,expir_date=expir_date,price=price,brand=brand)
        


    def update(self, Products=None):
        Products.name = self.cleaned_data['name']
        Products.kind = self.cleaned_data['kind']
        Products.descreption = self.cleaned_data['descreption']
        Products.expir_date = self.cleaned_data['expir_date']
        Products.price = self.cleaned_data['price']
        Products.brand = self.cleaned_data['brand']
        Products.save()