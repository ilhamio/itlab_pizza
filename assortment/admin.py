from django.contrib import admin

from assortment.models.coupon import Coupon
from assortment.models.drink import Drink
from assortment.models.pizza import Pizza


class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'diameter', 'description', 'is_active', 'created', 'updated']
    list_filter = ['is_active', 'created', 'updated']
    list_editable = ['price', 'diameter', 'is_active', 'description']
    prepopulated_fields = {'slug': ('name',)}


class DrinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'volume', 'description', 'is_active', 'created', 'updated']
    list_filter = ['is_active', 'created', 'updated']
    list_editable = ['price', 'volume', 'is_active']
    prepopulated_fields = {'slug': ('name',)}


class CouponAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'description', 'is_active', 'created', 'updated']
    list_filter = ['is_active', 'created', 'updated']
    list_editable = ['price', 'products', 'is_active']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Drink, DrinkAdmin)
admin.site.register(Coupon, CouponAdmin)
