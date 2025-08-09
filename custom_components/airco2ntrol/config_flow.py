"""Config flow for AirCO2ntrol integration."""
import logging
import voluptuous as vol

from homeassistant import config_entries
from . import DOMAIN
from .const import CONF_TEMPERATURE_OFFSET, DEFAULT_TEMPERATURE_OFFSET
from .const import CONF_HUMIDITY_OFFSET, DEFAULT_HUMIDITY_OFFSET

_LOGGER = logging.getLogger(__name__)

class AirCO2ntrolConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for AirCO2ntrol."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            return self.async_create_entry(
                title="AirCO2ntrol",
                data={
                    CONF_TEMPERATURE_OFFSET: user_input.get(CONF_TEMPERATURE_OFFSET, DEFAULT_TEMPERATURE_OFFSET),
                    CONF_HUMIDITY_OFFSET: user_input.get(CONF_HUMIDITY_OFFSET, DEFAULT_HUMIDITY_OFFSET),
                }
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Optional(CONF_TEMPERATURE_OFFSET, default=DEFAULT_TEMPERATURE_OFFSET): vol.Coerce(float),
                vol.Optional(CONF_HUMIDITY_OFFSET, default=DEFAULT_HUMIDITY_OFFSET): vol.Coerce(float),
            }),
            errors=errors,
        )

    @staticmethod
    def async_get_options_flow(config_entry):
        from .options_flow import AirCO2ntrolOptionsFlowHandler
        return AirCO2ntrolOptionsFlowHandler(config_entry)
