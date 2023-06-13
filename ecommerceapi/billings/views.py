"""
--> DONE <--
    -> Fazer a lógica de adicionar produtos em um determinado carrinho
    -> Fazer transição de carrinho(Car) pra Pedido(Order) ...

--> TODO <--
"""

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.response import Response, responses
from rest_framework.exceptions import ValidationError

from ecommerceapi.billings.models import Car, Order
from ecommerceapi.billings.models.cob import Cob
from ecommerceapi.billings.serializers import CarSerializer, OrderSerializer
from ecommerceapi.billings.exceptions import NonePkProvided
from ecommerceapi.billings.serializers.billings_serializer import CobSerializer
from ecommerceapi.core.commons import create, list, retrieve, update
from ecommerceapi.billings.controllers import BillingsController


class CarViewSet(viewsets.ViewSet):
    class Meta:
        model = Car

    def create(self, request):
        try:
            return Response(create(request.data, CarSerializer).data)
        except ValidationError:
            raise ValidationError("BAD Car information")

    def retrieve(self, request, pk: int = None):
        return Response(retrieve(Car.objects.all(), pk, CarSerializer).data)

    def list(self, request):
        return Response(list(Car.objects.all(), CarSerializer).data)

    def update(self, request, pk: int = None):
        return Response(update(request.data, Car.objects.all(), pk, CarSerializer).data)


class OrderViewSet(viewsets.ViewSet):
    class Meta:
        model = Order

    def transaction(self, request, pk: int):
        """
        Car to Order Transaction

        request have to has some data
        """
        car = get_object_or_404(Car.objects.all(), pk=pk)
        data = CarSerializer(car).data
        for k, v in request.data.items():
            data[k] = v

        serializer = OrderSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        car.delete()

        return Response(serializer.data)

    def retrieve(self, request, pk: int = None):
        return Response(retrieve(Order.objects.all(), pk, OrderSerializer).data)

    def list(self, request):
        return Response(list(Order.objects.all(), OrderSerializer).data)

    def finalize(self, request, pk: int) -> Response:
        """
        Finalizes a Billing Order and set the monitoring 
        delivery task queue
        """

        # TODO: implement payment feature here
        order = get_object_or_404(Order.objects.all(), pk=pk)
        order_serializer = OrderSerializer(data={"paid": True})
        order_serializer.is_valid()
        order_serializer.update(order, order_serializer.data)
        
        return Response(data={"message": "Order finalized successfully"})

    # There is no update
    # def update(self, request, pk: int=None):
    #     return Response(
    #         update(
    #             request.data, Order.objects.all(), pk, OrderSerializer
    #         ).data
    #     )


@csrf_exempt
def add_product(request, c_pk: int, pk: int) -> Response:
    """
    Adds a new Product on a determined car

    @param c_pk: Car id
    @param pl: product pk

    @return Response:
    """
    BillingsController.add_product(pk, c_pk)
    data = {"Success": "201"}
    return JsonResponse(data=data, status=201)


def create_cob(request, order_id: int) -> Response:
    order = get_object_or_404(Order.objects.first(), pk=order_id)
    boleto_data = BillingsController.emit_cob_boleto(cpf=order.cpf, value=order.price)
 
    data = {'value': order.price, 'order_id': order.id, 'status': 'approved',
            'boleto_id': boleto_data.get('id_boleto_individual'),
            'barcode': boleto_data.get('codigo_barras')}
    
    serializer = CobSerializer(data)
    serializer.is_valid()
    return serializer.create(serializer.data)
    
