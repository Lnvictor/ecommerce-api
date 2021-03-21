from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets, status, views
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from ecommerceapi.core.commons import create, list, retrieve, update
from ecommerceapi.core.exceptions import (
    InvalidProductInformation,
    InvalidDomainInformation,
)
from ecommerceapi.core.facade import get_products_from_domain
from ecommerceapi.core.models import Product, Domain
from ecommerceapi.core.serializers import ProductSerializer, DomainSerializer
from ecommerceapi.providers.models import Provider

from collections import deque
from decimal import Decimal


class DomainViewSet(viewsets.ViewSet):
    """
    Manages Domain Serializing control flow
    """

    @staticmethod
    def list(request, *args, **kwargs):
        return Response(list(Domain.objects.all(), DomainSerializer).data)

    @staticmethod
    def retrieve(request, pk=None, **kwargs):
        return Response(retrieve(Domain.objects.all(), pk, DomainSerializer).data)

    @staticmethod
    def create(request, *args, **kwargs):
        try:
            return Response(create(request.data, DomainSerializer))
        except ValidationError:
            raise InvalidDomainInformation()

    @staticmethod
    def update(request, pk=None, *args, **kwargs):
        try:
            return Response(
                update(request.data, Domain.objects.all(), pk, DomainSerializer).data
            )
        except ValidationError:
            raise InvalidDomainInformation()

    @staticmethod
    def destroy(request, pk=None, *args, **kwargs):
        domain = Domain.objects.filter(pk=pk).get()
        domain.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def get_products(self, pk=None):
        # -> Maybe this doesn't works very well
        import ipdb

        ipdb.sset_trace()
        serializer = ProductSerializer(get_products_from_domain(pk), many=True)

        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    class Meta:
        model = Product

    @staticmethod
    def list(request, *args, **kwargs):
        return Response(list(Product.objects.all(), ProductSerializer).data)

    @staticmethod
    def retrieve(request, pk=None, **kwargs):
        return Response(retrieve(Product.objects.all(), pk, ProductSerializer).data)

    @staticmethod
    def create(request, *args, **kwargs):
        try:
            return Response(create(request.data, ProductSerializer))
        except ValidationError:
            raise InvalidProductInformation()

    @staticmethod
    def update(request, pk=None, *args, **kwargs):
        try:
            return Response(
                update(request.data, Product.objects.all(), pk, ProductSerializer).data
            )
        except ValidationError:
            raise InvalidProductInformation()

    @staticmethod
    def destroy(request, pk=None, *args, **kwargs):
        product = Product.objects.filter(pk=pk).get()
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_products_from_provider(self, request, pk: int):
        """
        Get all products that one provider has been provided
        """

        provider = get_object_or_404(Provider.objects.all(), pk=pk)

        serializer = ProductSerializer(
            Product.objects.filter(provider=provider).all(), many=True
        )

        return Response(data=serializer.data)


class CsvFileViews(views.APIView):
    """
    This class contains methods to lead
    with csv files that provides products information.
    The aim here is load products from provided csv file
    and insert it into database.
    """

    @csrf_exempt
    def parse_csv(self, request):
        records = []
        text = deque(request.readlines())
        headers = text.popleft().decode("ascii").split(",")

        for record in text:
            tmp = {}
            attrs = record.decode("ascii").split(",")
            for i in range(len(headers)):
                header = headers[i].strip().strip("\n")
                numeric_headers = {"domain": int, "value": Decimal, "quantity": int}

                if header in numeric_headers.keys():
                    tmp[header] = numeric_headers[header](attrs[i].strip())
                else:
                    tmp[header] = attrs[i]

            records.append(tmp)

        serializer = ProductSerializer(data=records, many=True)
        serializer.is_valid()
        serializer.save()
        return JsonResponse(records, safe=False, status=201)
