from rest_framework import serializers

from ecommerceapi.billings.models import Car, Order
from ecommerceapi.billings.models.cob import Cob


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class CobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cob
        fields = "__all__"
