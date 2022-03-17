from django.urls import path, include

from order.router import router
from order.views.order import OrderRegisterAPIView, OrderCompleteAPIView, OrderFinishAPIView
from order.views.order_item import OrderItemCreateDestroyViewSet, OrderItemRetrieveUpdateViewSet

urlpatterns = [
    path('', include(router.urls)),  # CRUD for order
    path('<int:order_id>/register/', OrderRegisterAPIView.as_view()),  # changes status to 2 and is_registered true
    path('<int:order_id>/complete/', OrderCompleteAPIView.as_view()),  # changes status to 3
    path('<int:order_id>/finish/', OrderFinishAPIView.as_view()),  # Заказ переводится в архив

    path('<int:order_id>/add_product/', OrderItemCreateDestroyViewSet.as_view({'post': 'create'})),
    path('<int:order_id>/<slug:product>/', OrderItemRetrieveUpdateViewSet.as_view({'get': 'retrieve'})),
    path('<int:order_id>/<slug:product>/update_quantity/', OrderItemRetrieveUpdateViewSet.as_view({'put': 'update'})),
    path('<int:order_id>/<slug:product>/destroy', OrderItemCreateDestroyViewSet.as_view({'delete': 'destroy'})),
]
