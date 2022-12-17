"""The test for the HERE Travel Time integration."""

import pytest

from custom_components.open_route_service.config_flow import DEFAULT_OPTIONS
from custom_components.open_route_service.const import DOMAIN
from homeassistant.core import HomeAssistant

from .const import DEFAULT_CONFIG

from pytest_homeassistant_custom_component.common import MockConfigEntry


@pytest.mark.usefixtures("valid_response")
async def test_unload_entry(hass: HomeAssistant) -> None:
    """Test that unloading an entry works."""
    entry = MockConfigEntry(
        domain=DOMAIN,
        unique_id="0123456789",
        data=DEFAULT_CONFIG,
        options=DEFAULT_OPTIONS,
    )
    entry.add_to_hass(hass)

    await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    assert await hass.config_entries.async_unload(entry.entry_id)
    assert not hass.data[DOMAIN]
