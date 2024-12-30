"""Smart-me API client."""
from __future__ import annotations

import logging
from typing import Any

import aiohttp
from homeassistant.exceptions import HomeAssistantError

_LOGGER = logging.getLogger(__name__)

class SmartMeApiClient:
    """Smart-me API client."""

    def __init__(self, username: str, password: str) -> None:
        """Initialize the API client."""
        self.username = username
        self.password = password
        self.auth = aiohttp.BasicAuth(username, password)

    async def get_devices(self) -> list[dict[str, Any]]:
        """Get all devices for the account."""
        async with aiohttp.ClientSession() as session:
            url = "https://api.smart-me.com/Devices"
            async with session.get(url, auth=self.auth) as response:
                if response.status != 200:
                    raise InvalidAuth
                return await response.json()

    async def get_device(self, device_id: str) -> dict[str, Any]:
        """Get device data."""
        async with aiohttp.ClientSession() as session:
            url = f"https://smart-me.com:443/api/Devices/{device_id}"
            async with session.get(url, auth=self.auth) as response:
                if response.status != 200:
                    raise InvalidAuth
                return await response.json()

class InvalidAuth(HomeAssistantError):
    """Error to indicate there is invalid auth."""