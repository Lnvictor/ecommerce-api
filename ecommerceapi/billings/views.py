from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from ecommerceapi.billings.models import Car, Order
from ecommerceapi.billings.models.cob import Cob
from ecommerceapi.billings.serializers import CarSerializer, OrderSerializer
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

        order = get_object_or_404(Order.objects.all(), pk=pk)
        order_serializer = OrderSerializer(data={"paid": True})
        order_serializer.is_valid()
        order_serializer.update(order, order_serializer.data)
        
        return Response(data={"message": "Order finalized successfully"})


class CobViewSet(viewsets.ModelViewSet):
    class Meta:
        model = Cob
    
    serializer_class = CobSerializer

    def get_queryset(self):
        return Cob.objects.all()

    def create_cob(self, request, pk: int) -> Response:
        order = get_object_or_404(Order, pk=pk)
        boleto_data = BillingsController.emit_cob_boleto(cpf=order.cpf, value=order.price)
    
        data = {'value': order.price, 'order_id': order, 'status': 'approved',
                'boleto_id': boleto_data.get('id_boleto_individual'),
                'barcode': boleto_data.get('codigo_barras')}

        serializer = CobSerializer(data=data)
        serializer.is_valid()
        serializer.create(serializer.data)
        data['order_id'] = data['order_id'].pk
        return JsonResponse(data=data, status=201)


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
