import os
from django.db import models
from django.contrib.auth.models import User


class Size(models.Model):
    name_size = models.CharField(max_length=30)


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    article = models.IntegerField()
    prod_img = models.ImageField(upload_to=os.path.join('media/shop'), default=os.path.join('/media/shop/product.jpg'))


class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=True)


class CartItem(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ForeignKey(CartItem, blank=True, on_delete=models.CASCADE)
    total_price = models.FloatField()
