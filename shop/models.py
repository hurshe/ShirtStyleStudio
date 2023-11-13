import os
import secrets
import string

from django.db import models
from django.contrib.auth.models import User


class Size(models.Model):
    name_size = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name_size}"


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    article = models.CharField(max_length=10, unique=True, blank=True, null=True, editable=False)
    prod_img = models.ImageField(upload_to='media/shop', default='static/image/avatar.png')

    def save(self, *args, **kwargs):
        if not self.article:
            self.article = self.generate_unique_article()
        super(Product, self).save(*args, **kwargs)

    def generate_unique_article(self):
        random_number = ''.join(secrets.choice(string.digits) for _ in range(8))
        return random_number

    def __str__(self):
        return f"{self.title}"


class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=True)

    def __str__(self):
        return f"{self.product} price: {self.price}"


class CartItem(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.offer} qty: {self.quantity}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem, related_name='cart_items')
    total_price = models.FloatField(blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.total_price:
            self.total_price = self.update_total_price()
        super(Cart, self).save(*args, **kwargs)

    def update_total_price(self):
        cart_items = self.items.all()
        total = sum(item.offer.price * item.quantity for item in cart_items)
        return total

    def __str__(self):
        return f"Cart for user: {self.user} total: {self.total_price}"
