"""Smart-me API client."""
from __future__ import annotations

import logging
from typing import Any

import aiohttp

from .exceptions import InvalidAuth, ApiError
from .models import SmartMeDevice

_LOGGER = logging.getLogger(__name__)

class SmartMeApiClient:
    """Smart-me API client."""

    def __init__(self, username: str, password: str) -> None:
        """Initialize the API client."""
        self.username = username
        self.password = password
        self.auth = aiohttp.BasicAuth(username, password)

    async def get_devices(self) -> list[SmartMeDevice]:
        """Get all devices for the account."""
        try:
            async with aiohttp.ClientSession() as session:
                url = "https://api.smart-me.com/Devices"
                async with session.get(url, auth=self.auth) as response:
                    if response.status == 401:
                        raise InvalidAuth
                    if response.status != 200:
                        raise ApiError(f"API request failed with status {response.status}")
                    data = await response.json()
                    return [
                        SmartMeDevice(
                            id=device["Id"],
                            name=device["Name"],
                            serial=device["Serial"],
                        )
                        for device in data
                    ]
        except aiohttp.ClientError as err:
            raise ApiError(f"Failed to communicate with API: {err}") from err

    async def get_device(self, device_id: str) -> dict[str, Any]:
        """Get device data."""
        try:
            async with aiohttp.ClientSession() as session:
                url = f"https://smart-me.com:443/api/Devices/{device_id}"
                async with session.get(url, auth=self.auth) as response:
                    if response.status == 401:
                        raise InvalidAuth
                    if response.status != 200:
                        raise ApiError(f"API request failed with status {response.status}")
                    return await response.json()
        except aiohttp.ClientError as err:
            raise ApiError(f"Failed to communicate with API: {err}") from err