from django.contrib import admin

from coupon.models.coupon import Coupon


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_to', 'discount', 'active']
    search_fields = ['code']


admin.site.register(Coupon, CouponAdmin)
