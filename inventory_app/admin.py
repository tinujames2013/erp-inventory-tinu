from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Supplier, Stock, Order, OrderItem

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Stock)
admin.site.register(Order)
admin.site.register(OrderItem)
