import json
from decouple import config
import pytest
from django.test import Client
from django.urls import reverse
from rest_framework_api_key.models import APIKey


def create_sample_domain(name: str, desc: str, client: Client) -> dict:
    api_key, key = APIKey.objects.create_key(name="my-remote-service")
    data = {"name": name, "desc": desc}
    headers = {'HTTP_AUTHORIZATION': f'Api-Key {key}'}
    return client.post(reverse("core:domain"), data=json.dumps(data), **headers, content_type='Application/json')


@pytest.fixture
def resp_add_domain(client, db):
    return create_sample_domain("Fulano", "Teste", client)


@pytest.fixture
def resp_change_domain(resp_add_domain, client):
    api_key, key = APIKey.objects.create_key(name="my-remote-service")
    last_id = resp_add_domain.data.get("id")
    data = {"name": "Beltrano"}
    headers = {'HTTP_AUTHORIZATION': f'Api-Key {key}'}

    resp = client.put(
        reverse("core:domain_by_id", args=[last_id]),
        data=data,
        **headers,
        content_type="application/json",
    )

    return resp


@pytest.fixture
def resp_delete_domain(resp_add_domain, client, db):
    api_key, key = APIKey.objects.create_key(name="my-remote-service")
    headers = {'HTTP_AUTHORIZATION': f'Api-Key {key}'}
    last_id = resp_add_domain.data.get("id")
    resp = client.delete(
        reverse("core:domain_by_id", args=[last_id]), **headers, content_type="application/json"
    )

    return client.get(reverse("core:domain"), **headers)


def test_create_domain(resp_add_domain):
    assert resp_add_domain.data.get("name") == "Fulano"


def test_change_domain(resp_change_domain):
    assert resp_change_domain.data.get("name") == "Beltrano"


def test_delete_domain(resp_delete_domain):
    assert resp_delete_domain.data == []
