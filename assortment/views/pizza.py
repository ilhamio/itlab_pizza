from rest_framework.viewsets import ModelViewSet

from assortment.models.pizza import Pizza
from assortment.serializers.pizza import PizzaSerializer


class PizzaViewSet(ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
