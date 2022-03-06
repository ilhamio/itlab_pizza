from rest_framework import serializers

from assortment.models.pizza import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'
