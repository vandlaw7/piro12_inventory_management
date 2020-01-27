from django.forms import ModelForm
from shop.models import Product, Client


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
