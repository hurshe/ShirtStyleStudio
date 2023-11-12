from django.contrib import admin
from .models import Cart, CartItem, Product, Size, Offer
# Register your models here.


admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Offer)