import logging
import voluptuous as vol
from homeassistant import config_entries
from .const import CONF_TEMPERATURE_OFFSET, DEFAULT_TEMPERATURE_OFFSET
from .const import CONF_HUMIDITY_OFFSET, DEFAULT_HUMIDITY_OFFSET

_LOGGER = logging.getLogger(__name__)

class AirCO2ntrolOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle an option flow for AirCO2ntrol."""

    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        errors = {}

        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        data_schema = vol.Schema({
            vol.Optional(
                CONF_TEMPERATURE_OFFSET,
                default=self.config_entry.options.get(
                    CONF_TEMPERATURE_OFFSET,
                    self.config_entry.data.get(
                        CONF_TEMPERATURE_OFFSET,
                        DEFAULT_TEMPERATURE_OFFSET
                    )
                )
            ): vol.Coerce(float),
            vol.Optional(
                CONF_HUMIDITY_OFFSET,
                default=self.config_entry.options.get(
                    CONF_HUMIDITY_OFFSET,
                    self.config_entry.data.get(
                        CONF_HUMIDITY_OFFSET,
                        DEFAULT_HUMIDITY_OFFSET
                    )
                )
            ): vol.Coerce(float),
        })

        return self.async_show_form(
            step_id="init",
            data_schema=data_schema,
            errors=errors,
        )
