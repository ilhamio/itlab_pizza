from django.urls import path, include

from coupon.router import router

urlpatterns = [
    path('', include(router.urls))
]