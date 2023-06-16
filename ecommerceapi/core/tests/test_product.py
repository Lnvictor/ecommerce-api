import pytest
from django.urls import reverse

from ecommerceapi.core.tests.test_domain import create_sample_domain


@pytest.fixture
def resp_add_product(client, db, api_key):
    headers = {'HTTP_AUTHORIZATION': f'Api-Key {api_key}'}
    domain = create_sample_domain("Ciclano", "test", client, api_key)

    data = {
        "name": "Iphone 10",
        "desc": "balaco",
        "domain": domain.data.get('id'),
        "value": 110000.000,
        "quantity": 10,
    }

    return client.post(
        reverse("core:product"), data=data, **headers, content_type="application/json"
    )


@pytest.fixture
def resp_change_product(resp_add_product, client, db, api_key):
    headers = {'HTTP_AUTHORIZATION': f'Api-Key {api_key}'}
    data = {"desc": "test"}

    return client.put(
        reverse("core:product_by_id", args=[resp_add_product.data.get('id')]),
        data=data, **headers,
        content_type="application/json",
    )


@pytest.fixture
def resp_delete_product(resp_add_product, client, db, api_key):
    headers = {'HTTP_AUTHORIZATION': f'Api-Key {api_key}'}

    client.delete(
        reverse("core:product_by_id", args=[resp_add_product.data.get('id')]),
        **headers, content_type="application/json"
    )

    return client.get(reverse("core:product"), **headers)


def test_add_product(resp_add_product):
    assert resp_add_product.data.get("name") == "Iphone 10"


def test_change_product(resp_change_product):
    assert resp_change_product.data.get("desc") == "test"


def test_delete_product(resp_delete_product):
    assert resp_delete_product.data == []
