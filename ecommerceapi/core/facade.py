"""
Bussiness rules...
"""
from ecommerceapi.core.models import Domain, Product


def get_products_from_domain(domain: int):
    """
    Get all products for a given domain
    """
    import ipdb;ipdb.sset_trace()
    domain = Domain.objects.filter(pk=domain).get()
    return Product.objects.filter(domain=domain).all()
