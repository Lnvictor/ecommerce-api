"""

Billings Controller

@author Victor Pereira
"""
from django.shortcuts import get_object_or_404

from ecommerceapi.billings.models import Order
from ecommerceapi.billings.models.car import Car
from ecommerceapi.billings.serializers import OrderSerializer, CarSerializer
from ecommerceapi.core.models import Product


class BillingsController:
    """
    Controller for cart ans Order models
    """

    @staticmethod
    def get_price_of_car(products):
        return sum(
            [product['value'] for product in products]
        )

    @staticmethod
    def add_product(product_id: int, car_id: int):
        """
        Inserts given product to determined billings car

        @param product_id: Product to be inserted
        @param car_id: car to achieve the product
        @return: None
        """
        queryset_products = Product.objects.all()
        queryset_cars = Car.objects.all()
        product = get_object_or_404(queryset_products, product_id)
        car = get_object_or_404(queryset_cars, car_id)
        car.products.append(product)

    @staticmethod
    def get_status_from_correios(order_id):
        """
        TODO:
            Utilizar o celery para ficar checando o status no correios
            depois que o pedido for criado

        @param order_id:
        @return:
        """
        pass
