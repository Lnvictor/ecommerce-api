from django.db import models
from ecommerceapi.core.models.domain import Domain

from ecommerceapi.providers.models import Provider


class Product(models.Model):
    name = models.CharField(max_length=15, unique=True)
    desc = models.CharField(max_length=150)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    value = models.DecimalField(decimal_places=3, max_digits=15)
    quantity = models.IntegerField(default=0)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
