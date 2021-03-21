import json
import pytest
from django.test import Client
from django.urls import reverse


def create_sample_domain(name: str, desc: str, client: Client) -> dict:
    data = {"name": {name}, "desc": {desc}}
    return client.post(reverse("core:domain"), data=data)


@pytest.fixture
def resp_add_domain(client, db):
    return create_sample_domain("Fulano", "Teste", client)


@pytest.fixture
def resp_change_domain(resp_add_domain, client, db):
    last_id = resp_add_domain.data.get("id")
    data = {"name": "Beltrano"}

    resp = client.put(
        reverse("core:domain_by_id", args=[last_id]),
        data=data,
        content_type="application/json",
    )

    return resp


@pytest.fixture
def resp_delete_domain(resp_add_domain, client, db):
    last_id = resp_add_domain.data.get("id")
    resp = client.delete(
        reverse("core:domain_by_id", args=[last_id]), content_type="application/json"
    )

    return client.get(reverse("core:domain"))


def test_create_domain(resp_add_domain):
    assert resp_add_domain.data.get("name") == "Fulano"


def test_change_domain(resp_change_domain):
    assert resp_change_domain.data.get("name") == "Beltrano"


def test_delete_domain(resp_delete_domain):
    assert resp_delete_domain.data == []
