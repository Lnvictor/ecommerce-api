import pytest
from rest_framework_api_key.models import APIKey


@pytest.fixture
def api_key():
    try:
        key = APIKey.objects.get_from_key('my-remote-service')
    except APIKey.DoesNotExist:
        _, key = APIKey.objects.create_key(name="my-remote-service")
    
    return key