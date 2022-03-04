from rest_framework.response import Response

from assortment.serializers.pizza import PizzaSerializer


def serializing_data(data, instance=None):
    if instance:
        ser = PizzaSerializer(data=data, instance=instance)
    else:
        ser = PizzaSerializer(data=data)

    ser.is_valid(raise_exception=True)
    ser.save()

    return ser.data


