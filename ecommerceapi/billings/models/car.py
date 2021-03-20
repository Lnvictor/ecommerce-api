from django.db import models

from ecommerceapi.billings.controllers import BillingsController


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

    products = models.ManyToOneRel('core.Products', on_delete=models.CASCADE)
    price = models.DecimalField(
        default=BillingsController.get_price_of_car(products)
    )

