import pytest
from django.urls import reverse
from rest_framework_api_key.models import APIKey


@pytest.fixture
def resp(client, db):
    api_key, key = APIKey.objects.create_key(name="my-remote-service")
    headers = {'HTTP_AUTHORIZATION': f'Api-Key {key}'}
    return client.get(reverse("core:domain"), **headers)


def test_foo(resp):
    assert resp.status_code == 200
