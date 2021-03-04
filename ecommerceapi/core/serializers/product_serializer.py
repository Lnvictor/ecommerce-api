"""
Models  Serializers implementation

Serializers has the aim to convert objects to
json/xml and vice-versa

The implementation was made using django rest framework serializers
"""

from rest_framework import serializers

from ecommerceapi.core.models import Product, Domain


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'
