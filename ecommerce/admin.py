from django.contrib import admin
from .models import ProductImage, Shop,Product,Cart
# Register your models here.

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Cart)