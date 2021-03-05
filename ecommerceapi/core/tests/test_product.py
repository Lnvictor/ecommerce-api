import pytest
from django.urls import reverse

from ecommerceapi.core.tests.test_domain import create_sample_domain


@pytest.fixture
def resp_add_product(client, db):
    create_sample_domain("Ciclano", "test", client)

    data = {
        "name": "Iphone 10",
        "desc": "balaco",
        "domain": 1,
        "value": 110000.000,
        "quantity": 10
    }

    return client.post(
        reverse("core:product"),
        data=data,
        content_type="application/json"
    )


@pytest.fixture
def resp_change_product(resp_add_product, client, db):
    data = {
        "desc": "test"
    }

    return client.put(
        reverse('core:product_by_id', args=[1]),
        data=data,
        content_type="application/json"
    )


@pytest.fixture
def resp_delete_product(resp_add_product, client, db):
    client.delete(
        reverse('core:product_by_id', args=[1]),
        content_type="application/json"
    )

    return client.get(reverse("core:product"))


def test_add_product(resp_add_product):
    assert resp_add_product.data.get("name") == 'Iphone 10'


def test_change_product(resp_change_product):
    assert resp_change_product.data.get("desc") == 'test'


def test_delete_product(resp_delete_product):
    assert resp_delete_product.data == []


