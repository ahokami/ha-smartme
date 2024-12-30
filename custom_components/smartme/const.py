"""Constants for the Smart-me integration."""
from homeassistant.const import (
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_TIMESTAMP,
    ENERGY_KILO_WATT_HOUR,
    POWER_KILO_WATT,
    ELECTRIC_POTENTIAL_VOLT,
    ELECTRIC_CURRENT_AMPERE,
)

SCAN_INTERVAL = 30

SENSOR_TYPES = {
    "ActivePower": {
        "key": "ActivePower",
        "name": "Active Power",
        "device_class": DEVICE_CLASS_POWER,
        "unit": POWER_KILO_WATT,
    },
    "CounterReading": {
        "key": "CounterReading",
        "name": "Counter Reading",
        "device_class": DEVICE_CLASS_ENERGY,
        "unit": ENERGY_KILO_WATT_HOUR,
        "state_class": "total_increasing",
    },
    "Voltage": {
        "key": "Voltage",
        "name": "Voltage",
        "device_class": DEVICE_CLASS_VOLTAGE,
        "unit": ELECTRIC_POTENTIAL_VOLT,
    },
    # Add all other sensor types here...
}