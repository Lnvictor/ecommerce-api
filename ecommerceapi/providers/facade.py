"""
Provider's app business rules are implemented here
"""

from abc import ABC, abstractmethod

from ecommerceapi.providers.models import Provider


class ProviderController(ABC):
    @abstractmethod
    def get_products_from_api(self, provider: Provider) -> list:
        pass


class ProviderHook:
    def __init__(self, provider: Provider, provider_controller: ProviderController):
        self.provider = provider
        self.provider_controller = provider_controller

    def get_products_from_api(self):
        return self.provider_controller.get_products_from_api(self.provider)
