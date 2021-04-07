from django.db import models


class Order(models.Model):
    products = models.ManyToManyField("core.Product")
    address = models.JSONField()
    cpf = models.TextField(max_length=11)
    card_number = models.TextField(max_length=16)
    billing_type = models.TextChoices("Payment type", ("Debit", "Credit"))
    installments = models.IntegerField(default=None, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    paid = models.BooleanField(default=False)
    delivery_status = models.BooleanField(default=False)
    fiscal_note = models.TextField(max_length=14, null=True, default=None)
