from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from ecommerceapi.core.models import Product, Domain
from ecommerceapi.core.serializers import ProductSerializer


class DomainViewSet(viewsets.ModelViewSet):
    class Meta:
        model = Domain

    def list(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def delete(self):
        pass


class ProductViewSet(viewsets.ModelViewSet):
    class Meta:
        model = Product

    def list(self, request, *args, **kwargs):
        serializer = ProductSerializer(Product.objects.all(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        product = get_object_or_404(Product.objects.filter(pk=pk).get(), pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        product = Product.objects.filter(pk=pk).get()
        serializer.update(product, request.data)
        product.save()
        return Response(request.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        product = Product.objects.filter(pk=pk).get()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
