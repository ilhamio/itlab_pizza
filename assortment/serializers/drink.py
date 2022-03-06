from rest_framework import serializers

from assortment.models.drink import Drink


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'
