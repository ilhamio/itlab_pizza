from rest_framework.response import Response
from rest_framework.views import APIView

from assortment.models.pizza import Pizza
from assortment.serializers.pizza import PizzaSerializer
from assortment.views.utils import serializing_data


class PizzaAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """ Get single pizza by slug """
        slug = kwargs.get("slug", None)

        # if not slug:
        #     return Response({'error': 'Method GET not allowed'})
        #
        # try:
        #     instance = Pizza.objects.get(slug=slug)
        # except:
        #     return Response({'error': 'Object does not exists'})

        instance = get_instance_by_slug(slug, Pizza, 'GET')
        if type(instance) == Response:
            return instance

        return Response({'pizza': PizzaSerializer(instance).data})

    def post(self, request):
        """ Create new pizza """
        serialized_data = serializing_data(request.data)
        return Response({'new_pizza': serialized_data})

    def put(self, request, *args, **kwargs):
        """ Update pizza object """
        slug = kwargs.get("slug", None)

        if not slug:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Pizza.objects.get(slug=slug)
        except:
            return Response({'error': 'Object does not exists'})

        serialized_data = serializing_data(data=request.data, instance=instance)
        return Response({'edited pizza': serialized_data})

    def delete(self, request, *args, **kwargs):
        """Delete pizza object by slug"""
        slug = kwargs.get("slug", None)

        if not slug:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            instance = Pizza.objects.get(slug=slug)
            instance.delete()
        except:
            return Response({'error': 'Object does not exists'})

        return Response({'pizza': f'pizza with slug {slug} was deleted'})


def get_instance_by_slug(slug, model, method):
    if not slug:
        return Response({'error': f'Method {method} not allowed'})

    try:
        return model.objects.get(slug=slug)
    except:
        return Response({'error': 'Object does not exists'})