"""
Common Rest views behaviours

 (Created with the aim do not duplicated code)

"""

from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer

from ecommerceapi.core.exceptions import (
    InvalidDomainInformation,
    InvalidProductInformation,
)


def create(data, Serializer) -> ModelSerializer:
    serializer = Serializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.data


def list(queryset, Serializer) -> ModelSerializer:
    return Serializer(queryset, many=True)


def retrieve(queryset, pk, Serializer) -> ModelSerializer:
    obj = get_object_or_404(queryset, pk=pk)

    return Serializer(obj)


def update(data, queryset, pk, Serializer) -> ModelSerializer:
    obj = get_object_or_404(queryset, pk=pk)
    serializer = Serializer(data=data)
    serializer.is_valid()
    serializer.update(obj, data)

    return serializer
