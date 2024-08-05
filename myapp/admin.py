from django.contrib import admin
from .models import Product, BuyingOptions, Category

# Register your models here.

admin.site.register(Product)
admin.site.register(BuyingOptions)
admin.site.register(Category)