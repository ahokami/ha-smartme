"""Data update coordinator for Smart-me."""
from datetime import timedelta
import logging
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .api import SmartMeApiClient
from .const import DOMAIN, SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)

class SmartMeDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Smart-me data."""

    def __init__(
        self,
        hass: HomeAssistant,
        client: SmartMeApiClient,
        device_id: str,
    ) -> None:
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_{device_id}",
            update_interval=timedelta(seconds=SCAN_INTERVAL),
        )
        self.client = client
        self.device_id = device_id

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from Smart-me API."""
        return await self.client.get_device(self.device_id)