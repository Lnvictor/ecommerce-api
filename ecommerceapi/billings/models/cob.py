from django.db import models


class Cob(models.Model):
    value = models.DecimalField(decimal_places=2, max_digits=12, default=0.0, null=True)
    order_id = models.ForeignKey('billings.Order', on_delete=models.SET_NULL, null=True)
    status = models.Choices('cob_status', ('approved', 'paid', 'expired'))
    boleto_id = models.TextField(max_length=36, null=False)
    barcode = models.TextField(null=False)
