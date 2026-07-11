from __future__ import annotations

import requests
from requests.exceptions import ConnectionError, JSONDecodeError, Timeout

from utils.constants import (
    ERROR_TIMEOUT,
    ERROR_UNABLE_TO_REACH,
    ERROR_UNEXPECTED_RESPONSE,
    WEBHOOK_TIMEOUT_SECONDS,
)


class WebhookError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


def send_request(webhook_url: str, user_input: str) -> dict:
    payload = {"request": user_input}

    try:
        response = requests.post(
            webhook_url,
            json=payload,
            timeout=WEBHOOK_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
    except ConnectionError:
        raise WebhookError(ERROR_UNABLE_TO_REACH)
    except Timeout:
        raise WebhookError(ERROR_TIMEOUT)
    except requests.exceptions.RequestException:
        raise WebhookError(ERROR_UNABLE_TO_REACH)

    try:
        data = response.json()
    except (JSONDecodeError, ValueError):
        raise WebhookError(ERROR_UNEXPECTED_RESPONSE)

    if isinstance(data, list) and data:
        data = data[0]

    if not isinstance(data, dict):
        raise WebhookError(ERROR_UNEXPECTED_RESPONSE)

    return data
