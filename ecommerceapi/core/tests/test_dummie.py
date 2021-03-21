import pytest
from django.urls import reverse


@pytest.fixture
def resp(client, db):
    return client.get(reverse("core:domain"))


def test_foo(resp):
    assert resp.status_code == 200
