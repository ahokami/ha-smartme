"""Constants for the Smart-me integration."""
from homeassistant.components.sensor import (
    SensorDeviceClass,
)
from homeassistant.const import (
    PERCENTAGE,
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfPower,
)

DOMAIN = "smartme"
SCAN_INTERVAL = 30

SENSOR_TYPES = {
    # Power measurements
    "ActivePower": {
        "key": "ActivePower",
        "name": "Active Power",
        "device_class": SensorDeviceClass.POWER,
        "unit": UnitOfPower.KILO_WATT,
    },
    "ActivePowerL1": {
        "key": "ActivePowerL1",
        "name": "Active Power L1",
        "device_class": SensorDeviceClass.POWER,
        "unit": UnitOfPower.KILO_WATT,
    },
    "ActivePowerL2": {
        "key": "ActivePowerL2",
        "name": "Active Power L2",
        "device_class": SensorDeviceClass.POWER,
        "unit": UnitOfPower.KILO_WATT,
    },
    "ActivePowerL3": {
        "key": "ActivePowerL3",
        "name": "Active Power L3",
        "device_class": SensorDeviceClass.POWER,
        "unit": UnitOfPower.KILO_WATT,
    },
    
    # Energy readings
    "CounterReading": {
        "key": "CounterReading",
        "name": "Counter Reading",
        "device_class": SensorDeviceClass.ENERGY,
        "unit": UnitOfEnergy.KILO_WATT_HOUR,
        "state_class": "total_increasing",
    },
    "CounterReadingT1": {
        "key": "CounterReadingT1",
        "name": "Counter Reading T1",
        "device_class": SensorDeviceClass.ENERGY,
        "unit": UnitOfEnergy.KILO_WATT_HOUR,
        "state_class": "total_increasing",
    },
    "CounterReadingT2": {
        "key": "CounterReadingT2",
        "name": "Counter Reading T2",
        "device_class": SensorDeviceClass.ENERGY,
        "unit": UnitOfEnergy.KILO_WATT_HOUR,
        "state_class": "total_increasing",
    },
    "CounterReadingImport": {
        "key": "CounterReadingImport",
        "name": "Counter Reading Import",
        "device_class": SensorDeviceClass.ENERGY,
        "unit": UnitOfEnergy.KILO_WATT_HOUR,
        "state_class": "total_increasing",
    },
    "CounterReadingExport": {
        "key": "CounterReadingExport",
        "name": "Counter Reading Export",
        "device_class": SensorDeviceClass.ENERGY,
        "unit": UnitOfEnergy.KILO_WATT_HOUR,
        "state_class": "total_increasing",
    },
    
    # Voltage measurements
    "Voltage": {
        "key": "Voltage",
        "name": "Voltage",
        "device_class": SensorDeviceClass.VOLTAGE,
        "unit": UnitOfElectricPotential.VOLT,
    },
    "VoltageL1": {
        "key": "VoltageL1",
        "name": "Voltage L1",
        "device_class": SensorDeviceClass.VOLTAGE,
        "unit": UnitOfElectricPotential.VOLT,
    },
    "VoltageL2": {
        "key": "VoltageL2",
        "name": "Voltage L2",
        "device_class": SensorDeviceClass.VOLTAGE,
        "unit": UnitOfElectricPotential.VOLT,
    },
    "VoltageL3": {
        "key": "VoltageL3",
        "name": "Voltage L3",
        "device_class": SensorDeviceClass.VOLTAGE,
        "unit": UnitOfElectricPotential.VOLT,
    },
    
    # Current measurements
    "CurrentL1": {
        "key": "CurrentL1",
        "name": "Current L1",
        "device_class": SensorDeviceClass.CURRENT,
        "unit": UnitOfElectricCurrent.AMPERE,
    },
    "CurrentL2": {
        "key": "CurrentL2",
        "name": "Current L2",
        "device_class": SensorDeviceClass.CURRENT,
        "unit": UnitOfElectricCurrent.AMPERE,
    },
    "CurrentL3": {
        "key": "CurrentL3",
        "name": "Current L3",
        "device_class": SensorDeviceClass.CURRENT,
        "unit": UnitOfElectricCurrent.AMPERE,
    },
    
    # Power factor measurements
    "PowerFactor": {
        "key": "PowerFactor",
        "name": "Power Factor",
        "unit": PERCENTAGE,
    },
    "PowerFactorL1": {
        "key": "PowerFactorL1",
        "name": "Power Factor L1",
        "unit": PERCENTAGE,
    },
    "PowerFactorL2": {
        "key": "PowerFactorL2",
        "name": "Power Factor L2",
        "unit": PERCENTAGE,
    },
    "PowerFactorL3": {
        "key": "PowerFactorL3",
        "name": "Power Factor L3",
        "unit": PERCENTAGE,
    },
    
    # Digital output status
    "DigitalOutput2": {
        "key": "DigitalOutput2",
        "name": "Digital Output 2",
    },
    
    # Timestamp
    "ValueDate": {
        "key": "ValueDate",
        "name": "Last Update",
        "device_class": SensorDeviceClass.TIMESTAMP,
    },
}