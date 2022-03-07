from django.contrib import admin

from coupon.models.coupon import Coupon
from assortment.models.category import Category
from assortment.models.product import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'size', 'description', 'is_active', 'created', 'updated']
    list_filter = ['is_active', 'created', 'updated']
    list_editable = ['price', 'size', 'is_active', 'description']
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
