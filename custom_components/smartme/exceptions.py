"""Exceptions for Smart-me integration."""
from homeassistant.exceptions import HomeAssistantError

class SmartMeError(HomeAssistantError):
    """Base class for Smart-me exceptions."""

class InvalidAuth(SmartMeError):
    """Error to indicate there is invalid auth."""

class ApiError(SmartMeError):
    """Error to indicate API communication issues."""