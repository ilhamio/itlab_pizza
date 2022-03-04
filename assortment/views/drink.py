from rest_framework.response import Response
from rest_framework.views import APIView

from assortment.models.drink import Drink
from assortment.serializers.drink import DrinkSerializer
from assortment.views.utils import serializing_data


class DrinkAPIView(APIView):

    def post(self, request):
        serialized_data = serializing_data(request.data)
        return Response({'new_drink': serialized_data})

    def put(self, request, *args, **kwargs):
        slug = kwargs.get("slug", None)

        if not slug:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Drink.objects.get(slug=slug)
        except:
            return Response({'error': 'Object does not exists'})

        serialized_data = serializing_data(data=request.data, instance=instance)
        return Response({'edited pizza': serialized_data})
