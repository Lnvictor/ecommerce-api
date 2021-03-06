"""
Bussiness rules...
"""

from ecommerceapi.core.models import Domain, Product


def get_products_from_domain(domain: int):
    """
    Get all products for a given domain
    """

    domain = Domain.objects.filter(pk=domain).get()
    return Product.objects.filter(domain=domain).all()


def get_products_from_csv_file(file):
    # TODO: Aprender como lidar com arquivos de upload no django
    pass