"""Tests for open_route_service."""
import pytest
import os
import json

from homeassistant.const import ATTR_ICON, EVENT_HOMEASSISTANT_START
from homeassistant.setup import async_setup_component

from pytest_homeassistant_custom_component.async_mock import patch
from pytest_homeassistant_custom_component.common import async_fire_time_changed


def load_fixture(filename):
    """Load a fixture."""
    path = os.path.join(os.path.dirname(__file__), "fixtures", filename)
    with open(path, encoding="utf-8") as fptr:
        return fptr.read()


async def test_sensor(hass):
    """Test that sensor works."""
    with patch(
        "openrouteservice.Client.directions",
        return_value=json.loads(load_fixture("directions_response.json")),
    ):
        with patch(
            "openrouteservice.Client.pelias_reverse",
            return_value=json.loads(load_fixture("reverse_geocode_response.json")),
        ):
            config = {
                "sensor": {
                    "platform": "open_route_service",
                    "origin_latitude": "51.222975",
                    "origin_longitude": "9.267577",
                    "destination_latitude": "51.257430",
                    "destination_longitude": "9.335892",
                    "api_key": "test",
                }
            }
            assert await async_setup_component(hass, "sensor", config)
            await hass.async_block_till_done()

            hass.bus.async_fire(EVENT_HOMEASSISTANT_START)
            await hass.async_block_till_done()

            sensor = hass.states.get("sensor.openroute_service_travel_time")
            assert sensor.state == "4"


async def test_sensor_origin_destination_are_same(hass):
    """Test that sensor works when origin and destionation are the same."""
    with patch(
        "openrouteservice.Client.directions",
        return_value=json.loads(
            load_fixture("directions_response_origin_destination_are_same.json")
        ),
    ):
        with patch(
            "openrouteservice.Client.pelias_reverse",
            return_value=json.loads(load_fixture("reverse_geocode_response.json")),
        ):
            config = {
                "sensor": {
                    "platform": "open_route_service",
                    "origin_latitude": "51.222975",
                    "origin_longitude": "9.267577",
                    "destination_latitude": "51.257430",
                    "destination_longitude": "9.335892",
                    "api_key": "test",
                }
            }
            assert await async_setup_component(hass, "sensor", config)
            await hass.async_block_till_done()

            hass.bus.async_fire(EVENT_HOMEASSISTANT_START)
            await hass.async_block_till_done()

            sensor = hass.states.get("sensor.openroute_service_travel_time")
            assert sensor.state == "0"
