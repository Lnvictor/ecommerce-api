from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from ecommerceapi.core.models import Product, Domain
from ecommerceapi.core.serializers import ProductSerializer, DomainSerializer


class DomainViewSet(viewsets.ViewSet):
    """
    Manages Domain Serializing control flow
    """

    @staticmethod
    def list(request, *args, **kwargs):
        queryset = Domain.objects.all()
        serializer = DomainSerializer(queryset, many=True)

        return Response(serializer.data)

    @staticmethod
    def retrieve(request, pk=None, **kwargs):
        queryset = Domain.objects.all()
        domain = get_object_or_404(queryset, pk=pk)
        serializer = DomainSerializer(domain)

        return Response(serializer.data)

    @staticmethod
    def create(request, *args, **kwargs):
        serializer = DomainSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

    @staticmethod
    def update(request, pk=None, *args, **kwargs):
        queryset = Domain.objects.all()
        domain = get_object_or_404(queryset, pk=pk)
        serializer = DomainSerializer(domain)
        serializer.update(domain, request.data)

        return Response(serializer.data)

    @staticmethod
    def destroy(request, pk=None, *args, **kwargs):
        domain = Domain.objects.filter(pk=pk).get()
        domain.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductViewSet(viewsets.ViewSet):
    class Meta:
        model = Product

    @staticmethod
    def list(request, *args, **kwargs):
        serializer = ProductSerializer(Product.objects.all(), many=True)
        return Response(serializer.data)

    @staticmethod
    def retrieve(request, pk=None, **kwargs):
        product = get_object_or_404(Product.objects.filter(pk=pk).get(), pk=pk)
        serializer = ProductSerializer(product)

        return Response(serializer.data)

    @staticmethod
    def create(request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

    @staticmethod
    def update(request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        product = Product.objects.filter(pk=pk).get()
        serializer.update(product, request.data)
        product.save()

        return Response(request.data)

    @staticmethod
    def destroy(request, pk=None, *args, **kwargs):
        product = Product.objects.filter(pk=pk).get()
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
