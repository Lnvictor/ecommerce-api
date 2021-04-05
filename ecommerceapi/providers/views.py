"""
Provider's app views implementation
"""
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from ecommerceapi.providers.ProviderHooks import giant_bomb_hook
from ecommerceapi.providers.exceptions import InvalidProviderData
from ecommerceapi.providers.models import Provider
from ecommerceapi.providers.serializers.provider_serializer import ProviderSerializer


class ProviderViewSet(viewsets.ViewSet):
    """
    Provider models viewset implementation
    """

    def list(self, request):
        serializer = ProviderSerializer(Provider.objects.all(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk: int = None):
        queryset = Provider.objects.all()
        provider = get_object_or_404(queryset, pk=pk)
        serializer = ProviderSerializer(provider)

        return Response(serializer.data)

    def create(self, request):
        serializer = ProviderSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            raise InvalidProviderData()

        serializer.save()

        return Response(serializer.data)

    def update(self, request, pk: int = None):
        queryset = Provider.objects.all()
        provider = get_object_or_404(queryset, pk=pk)
        serializer = ProviderSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            raise InvalidProviderData()

        serializer.update(provider, request.data)
        provider.save()

        return Response(serializer.data)

    def destroy(self, pk: int = None):
        queryset = Provider.objects.all()
        provider = get_object_or_404(queryset, pk=pk)
        provider.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def products_from_api(request):
    return JsonResponse(giant_bomb_hook.get_products_from_api(), status=201, safe=False)
