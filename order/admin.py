from django.contrib import admin

from order.models.order import Order
from order.models.order_item import OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name_in_queue', 'created', 'updated', 'paid', 'is_registered']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)