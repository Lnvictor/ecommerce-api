"""
Bussiness rules...
"""

from ecommerceapi.core.models import Domain, Product


def export_product_by_id(pk: int) -> Product:
    return Product.objects.filter(pk=pk).get()


def get_products_from_domain(domain: int):
    """
    Get all products for a given domain
    """

    domain = Domain.objects.filter(pk=domain).get()
    return Product.objects.filter(domain=domain).all()


class CsvFileHandler:
    def parse_products_from_csv_file(self, file):
        pass
