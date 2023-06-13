"""
Billings Controller

@author Victor Pereira
"""

from django.shortcuts import get_object_or_404
import requests

from ecommerceapi import settings
from ecommerceapi.billings.models import Car
from ecommerceapi.billings.utils import _get_itau_request_headers, _get_itau_request_payload
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
    
    @staticmethod
    def emit_cob_boleto(cpf: str, value: float) -> dict:
        headers = _get_itau_request_headers()
        payload = _get_itau_request_payload(cpf=cpf)
        emit_boleto_url = f'{settings.ITAU_API_BASE_URL}/itau-ep9-gtw-cash-management-ext-v2/v2/boletos'

        response = requests.post(url=emit_boleto_url, json=payload, headers=headers)

        return response.json()['dados_individuais_boleto'][0]
