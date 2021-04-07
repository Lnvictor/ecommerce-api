"""
Billings Controller

@author Victor Pereira
"""

from django.shortcuts import get_object_or_404

from ecommerceapi.billings.models import Car, Order
from ecommerceapi.billings.serializers import OrderSerializer, CarSerializer
from ecommerceapi.core.models import Product


class BillingsController:
    """
    Controller for cart ans Order models
    """

    @staticmethod
    def get_price_of_car(products):
        return sum([product["value"] for product in products])

    @staticmethod
    def add_product(product_id: int, car_id: int) -> None:
        """
        Inserts given product to determined billings car

        @param product_id: Product to be inserted
        @param car_id: car to achieve the product
        @return: None
        """
        car = get_object_or_404(Car.objects.all(), pk=car_id)
        car.products.add(product_id)
        car.price += get_object_or_404(Product.objects.all(), pk=product_id).value
        car.save()
