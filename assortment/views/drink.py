from rest_framework.viewsets import ModelViewSet

from assortment.models.drink import Drink
from assortment.serializers.drink import DrinkSerializer


class DrinkViewSet(ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
