"""Config flow for Smart-me integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult

from .api import SmartMeApiClient
from .exceptions import InvalidAuth, ApiError
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class SmartMeConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Smart-me."""

    VERSION = 1

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

        errors = {}

        try:
            client = SmartMeApiClient(
                user_input[CONF_USERNAME],
                user_input[CONF_PASSWORD],
            )
            devices = await client.get_devices()
        except InvalidAuth:
            errors["base"] = "invalid_auth"
        except ApiError:
            errors["base"] = "cannot_connect"
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Unexpected exception")
            errors["base"] = "unknown"
        else:
            await self.async_set_unique_id(user_input[CONF_USERNAME])
            self._abort_if_unique_id_configured()
            
            return self.async_create_entry(
                title=f"Smart-me ({len(devices)} devices)",
                data={
                    CONF_USERNAME: user_input[CONF_USERNAME],
                    CONF_PASSWORD: user_input[CONF_PASSWORD],
                    "devices": [
                        {
                            "id": device.id,
                            "name": device.name,
                            "serial": device.serial,
                        }
                        for device in devices
                    ],
                },
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_USERNAME): str,
                    vol.Required(CONF_PASSWORD): str,
                }
            ),
            errors=errors,
        )