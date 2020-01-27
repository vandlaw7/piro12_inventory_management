from django.db import models
from django.urls import reverse


class Client(models.Model):
    name = models.CharField(max_length=40, verbose_name='이름')
    phone = models.CharField(max_length=40, verbose_name='전화번호')
    address = models.CharField(max_length=100, verbose_name='주소')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:detail_client', args=[self.pk])


class Product(models.Model):
    name = models.CharField(max_length=40, verbose_name='제품명')
    photo = models.ImageField(upload_to='', verbose_name='제품사진')
    desc = models.TextField(verbose_name='제품설명')
    price = models.IntegerField(verbose_name='가격')
    stock = models.IntegerField(verbose_name='남은수량')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='거래처', related_name='product')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:detail_product', args=[self.pk])
