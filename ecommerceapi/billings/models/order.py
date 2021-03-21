from django.db import models


class Order(models.Model):
    products = models.ManyToManyField("core.Product")
    address = models.JSONField()
    price = models.DecimalField(decimal_places=2, max_digits=15)
    correios_code = models.TextField()
    delivery_status = models.BooleanField()
