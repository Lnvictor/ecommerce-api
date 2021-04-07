from decouple import config
import requests

from ecommerceapi.core.models import Domain
from ecommerceapi.providers.exceptions import NotFoundProvider
from ecommerceapi.providers.facade import ProviderController, ProviderHook
from ecommerceapi.providers.models import Provider

from typing import List

API_URL = "http://www.giantbomb.com/api/games/"
API_KEY = config("GIANT_BOMB_API_KEY")
GAMES_DOMAIN = Domain.objects.filter(name="Games").first()

def save_product_data(data: dict) -> bool:
    # import ipdb;ipdb.sset_trace()

    try:
        provider = Provider.giant_bomb.all()[0].id
    except IndexError:
        # If Index error raises, its because Giant Bomb does not
        # exists in the database, then we raises not found
        # Provider exception
        raise NotFoundProvider("GiantBomb provider must be created first")

    # Persisting data
    request_data = {
        "name": data["name"],
        "desc": data["deck"],
        "domain": GAMES_DOMAIN,
        "quantity": 0,
        "value": 0.0,
        "provider": provider,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": config('REST_KEY')
    }

    requests.post("http://localhost:8000/product/", json=request_data, headers=headers)

    return True


class GiantBombController(ProviderController):
    def get_products_from_api(self) -> List:
        params = {"api_key": API_KEY, "format": "json"}
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-type": "application/json",
            "Authorization": API_KEY,
        }
        response = requests.get(API_URL, params=params, headers=headers)
        data = response.json()["results"]

        for el in data:
            try:
                save_product_data(el)
            except NotFoundProvider:
                return []

        return data


# Singleton
giant_bomb_hook = ProviderHook(GiantBombController())
