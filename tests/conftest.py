"""Global fixtures for open_route_service integration."""
import json
import os
from unittest.mock import patch

import pytest

pytest_plugins = "pytest_homeassistant_custom_component"  # pylint: disable=invalid-name

@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Enable custom integration loading."""
    yield

@pytest.fixture(name="valid_response")
def valid_response_fixture():
    """Return valid api response."""
    with patch(
        "openrouteservice.Client.directions", return_value=load_json_fixture("directions_response.json")
    ), patch(
        "openrouteservice.Client.pelias_reverse",
        return_value=load_json_fixture("reverse_geocode_response.json"),
    ) as mock:
        yield mock


def load_json_fixture(filename: str) -> str:
    """Load a fixture."""
    path = os.path.join(os.path.dirname(__file__), "fixtures", filename)
    with open(path, encoding="utf-8") as fptr:
        return fptr.read()