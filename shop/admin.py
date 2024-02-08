# admin.py
from django.contrib import admin
from .models import Cagagory, Product

class CagagoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'status', 'created_at')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor', 'quantity', 'original_price', 'selling_price', 'status', 'trending', 'created_at')

admin.site.register(Cagagory, CagagoryAdmin)
admin.site.register(Product, ProductAdmin)
