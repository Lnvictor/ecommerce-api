from django.db import models


class Order(models.Model):
    products = models.ManyToOneRel('core.Product', on_delete=models.CASCADE)
    address = models.JSONField()
    total_value = models.DecimalField(decimal_places=2)
    correios_code = models.TextField()
    delivery_status = models.BooleanField()
