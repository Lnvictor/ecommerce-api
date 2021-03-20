"""
TODO
    -> Fazer transição de carrinho(Car) pra Pedido(Order)
"""

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from ecommerceapi.billings.models import Car, Order
from ecommerceapi.billings.serializers import CarSerializer, OrderSerializer
from ecommerceapi.billings.exceptions import NonePkProvided
from ecommerceapi.core.commons import create, list, retrieve, update


class CarViewSet(viewsets.ViewSet):
    class Meta:
        model = Car


    def create(self, request):
        try:
            return Response(
                create(request.data, CarSerializer).data
            )
        except ValidationError:
            raise ValidationError('BAD Car information')
    
    def retrieve(self, request, pk: int=None):
        return Response(
            retrieve(
                Car.objects.all(), pk, CarSerializer
            ).data
        )

    def list(self, request):
        return Response(
            list(
                Car.objects.all(), CarSerializer
            ).data
        )

    def update(self, request, pk: int=None):
        return Response(
            update(
                request.data, Car.objects.all(), pk, CarSerializer
            ).data
        )

            

class OrderViewSet(viewsets.ViewSet):
    class Meta:
        model = Order


    def create(self, request):
        try:
            return Response(
                create(request.data, OrderSerializer).data
            )
        except ValidationError:
            raise ValidationError('BAD Order information')
    
    def retrieve(self, request, pk: int=None):
        return Response(
            retrieve(
                Order.objects.all(), pk, OrderSerializer
            ).data
        )

    def list(self, request):
        return Response(
            list(
                Order.objects.all(), OrderSerializer
            ).data
        )

    def update(self, request, pk: int=None):
        return Response(
            update(
                request.data, Order.objects.all(), pk, OrderSerializer
            ).data
        )