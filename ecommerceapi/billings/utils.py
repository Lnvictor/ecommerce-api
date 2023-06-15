from datetime import datetime

import requests

from ecommerceapi import settings


__ITAU_HEADERS = {"x-itau-apikey": "123"}
ACCESS_TOKEN_EXPIRES_IN = 300  # seconds


def __generate_itau_access_token() -> str:
    if "x-sandbox-token" in __ITAU_HEADERS.keys():
        time_diff = datetime.now() - datetime.fromisoformat(
            __ITAU_HEADERS.get("access_token_created_at")
        )
        if time_diff.total_seconds() <= ACCESS_TOKEN_EXPIRES_IN:
            return

    payload = {
        "client_id": settings.ITAU_API_CLIENT_ID,
        "client_secret": settings.ITAU_API_CLIENT_SECRET,
    }
    url = f"{settings.ITAU_API_BASE_URL}/api/jwt"
    response = requests.post(url=url, json=payload)

    __ITAU_HEADERS["x-sandbox-token"] = response.json()["access_token"]
    __ITAU_HEADERS["access_token_created_at"] = datetime.now().isoformat()


def _get_itau_request_headers() -> dict:
    __generate_itau_access_token()
    return __ITAU_HEADERS


def _get_itau_request_payload(cpf: str) -> dict:
    pass
