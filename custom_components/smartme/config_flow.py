"""Config flow for Smart-me integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult

from .api import InvalidAuth, SmartMeApiClient
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Smart-me."""

    VERSION = 1

    def __init__(self) -> None:
        """Initialize flow."""
        self.username: str | None = None
        self.password: str | None = None
        self.devices: list[dict[str, Any]] = []

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle username/password step."""
        if user_input is None:
            return self.async_show_form(
                step_id="user",
                data_schema=vol.Schema(
                    {
                        vol.Required(CONF_USERNAME): str,
                        vol.Required(CONF_PASSWORD): str,
                    }
                ),
            )

        self.username = user_input[CONF_USERNAME]
        self.password = user_input[CONF_PASSWORD]

        try:
            client = SmartMeApiClient(self.username, self.password)
            self.devices = await client.get_devices()
        except InvalidAuth:
            return self.async_show_form(
                step_id="user",
                data_schema=vol.Schema(
                    {
                        vol.Required(CONF_USERNAME): str,
                        vol.Required(CONF_PASSWORD): str,
                    }
                ),
                errors={"base": "invalid_auth"},
            )

        return await self.async_step_devices()

    async def async_step_devices(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle device selection step."""
        if user_input is None:
            device_schema = vol.Schema(
                {
                    vol.Required(device["Id"]): bool
                    for device in self.devices
                }
            )

            return self.async_show_form(
                step_id="devices",
                data_schema=device_schema,
                description_placeholders={
                    f"device_{device['Id']}": f"{device['Name']} ({device['Serial']})"
                    for device in self.devices
                },
            )

        selected_devices = [
            device for device in self.devices
            if user_input.get(device["Id"], False)
        ]

        if not selected_devices:
            return self.async_show_form(
                step_id="devices",
                data_schema=vol.Schema(
                    {
                        vol.Required(device["Id"]): bool
                        for device in self.devices
                    }
                ),
                errors={"base": "no_devices_selected"},
            )

        return self.async_create_entry(
            title=f"Smart-me ({len(selected_devices)} devices)",
            data={
                CONF_USERNAME: self.username,
                CONF_PASSWORD: self.password,
                "devices": [
                    {
                        "id": device["Id"],
                        "name": device["Name"],
                        "serial": device["Serial"],
                    }
                    for device in selected_devices
                ],
            },
        )