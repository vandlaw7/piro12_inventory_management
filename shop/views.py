from django.shortcuts import render, redirect
from django.urls import reverse

from shop.models import Product, Client
from .forms import ProductForm, ClientForm


def list_product(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'shop/list_product.html', context)


def list_client(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'shop/list_client.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
        return redirect(product)
    else:
        form = ProductForm()
        context = {
            'form': form
        }
    return render(request, 'shop/create_product.html', context)


def change_stock(request, pk, value):
    if value == 1:
        product = Product.objects.get(pk=pk)
        product.stock += 1
        product.save()
    if value == 2:
        product = Product.objects.get(pk=pk)
        product.stock -= 1
        product.save()
    return redirect('shop:list_product')


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
        return redirect(client)
    else:
        form = ClientForm()
        context = {
            'form': form
        }
        return render(request, 'shop/create_client.html', context)


def detail_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'shop/detail_product.html', context)


def detail_client(request, pk):
    client = Client.objects.get(pk=pk)
    products = client.product.all()
    context = {
        'client': client,
        'products': products,
    }
    return render(request, 'shop/detail_client.html', context)


def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('shop:list_product')


def delete_client(request, pk):
    client = Client.objects.get(pk=pk)
    client.delete()
    return redirect('shop:list_client')


def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
        return redirect(product)

    else:
        form = ProductForm(instance=product)
        context = {
            'form': form
        }
        return render(request, 'shop/create_product.html', context)


def edit_client(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
        return redirect(client)
    else:
        form = ClientForm(instance=client)
        context = {
            'form': form
        }
        return render(request, 'shop/create_client.html', context)
