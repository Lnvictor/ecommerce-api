from django.db import models


class Car(models.Model):
    """
    Car is a collection of products that
    the customer can group and view the
    current status of your selected products
    chosen.

    When the customer ask for finalize the
    order, then the Car will be passed to
    Order model, also specifies in this app.
    """

    products = models.ManyToManyField("core.Product")
    price = models.DecimalField(decimal_places=2, max_digits=15)
