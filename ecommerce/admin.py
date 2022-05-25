from django.contrib import admin
from .models import ProductImage, Shop,Product,Cart,Order,OrderItem
# Register your models here.

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)