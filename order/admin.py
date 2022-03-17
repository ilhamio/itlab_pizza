from django.contrib import admin

from archive.models.archive_order import ArchiveOrder
from order.models.order import Order
from order.models.order_item import OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name_in_queue', 'created', 'updated', 'paid', 'is_registered']
    inlines = [OrderItemInline]


class ArchiveOrderAdmin(admin.ModelAdmin):
    list_display = ['name_in_queue', 'created', 'cost', 'coupon']


admin.site.register(Order, OrderAdmin)
admin.site.register(ArchiveOrder, ArchiveOrderAdmin)
