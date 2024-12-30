"""Data models for Smart-me integration."""
from dataclasses import dataclass
from typing import Any

@dataclass
class SmartMeDevice:
    """Smart-me device data model."""
    id: str
    name: str
    serial: str
    
@dataclass
class SmartMeSensorType:
    """Smart-me sensor type data model."""
    key: str
    name: str
    device_class: str | None = None
    unit: str | None = None
    state_class: str | None = None