from rest_framework.generics import ListAPIView

from assortment.models.drink import Drink
from assortment.models.pizza import Pizza
from assortment.serializers.drink import DrinkSerializer
from assortment.serializers.pizza import PizzaSerializer


class DrinkListAPIView(ListAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


class PizzaListAPIView(ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
