from django.contrib import admin

from .models import Product, ProductImage, Shop, ShopImage, Category


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Shop)
admin.site.register(ShopImage)
admin.site.register(Category)
