"""Support for Smart-me sensors."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .api import SmartMeApiClient
from .const import DOMAIN, SENSOR_TYPES
from .coordinator import SmartMeDataUpdateCoordinator

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Smart-me sensors."""
    client = SmartMeApiClient(
        entry.data[CONF_USERNAME],
        entry.data[CONF_PASSWORD],
    )

    entities = []
    
    for device in entry.data["devices"]:
        coordinator = SmartMeDataUpdateCoordinator(
            hass,
            client,
            device["id"],
        )
        await coordinator.async_config_entry_first_refresh()

        for sensor_type in SENSOR_TYPES.values():
            entities.append(
                SmartMeSensor(
                    coordinator,
                    device,
                    sensor_type,
                )
            )

    async_add_entities(entities)

class SmartMeSensor(CoordinatorEntity, SensorEntity):
    """Representation of a Smart-me sensor."""

    def __init__(
        self,
        coordinator: SmartMeDataUpdateCoordinator,
        device: dict,
        sensor_type: dict,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        
        self._device = device
        self._sensor_type = sensor_type
        
        self._attr_name = f"{device['name']} {sensor_type['name']}"
        self._attr_unique_id = f"{device['id']}_{sensor_type['key']}"
        self._attr_device_class = sensor_type.get("device_class")
        self._attr_native_unit_of_measurement = sensor_type.get("unit")
        self._attr_state_class = sensor_type.get("state_class")
        
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device["id"])},
            name=device["name"],
            manufacturer="Smart-me",
            model="Smart Meter",
            serial_number=str(device["serial"]),
        )

    @property
    def native_value(self) -> StateType:
        """Return the state of the sensor."""
        return self.coordinator.data.get(self._sensor_type["key"])
