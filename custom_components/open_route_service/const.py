"""Constants for open_route_service."""
CONF_DESTINATION_LATITUDE = "destination_latitude"
CONF_DESTINATION_LONGITUDE = "destination_longitude"
CONF_DESTINATION_ENTITY_ID = "destination_entity_id"
CONF_ORIGIN_LATITUDE = "origin_latitude"
CONF_ORIGIN_LONGITUDE = "origin_longitude"
CONF_ORIGIN_ENTITY_ID = "origin_entity_id"
CONF_ROUTE_MODE = "route_mode"
CONF_ORIGIN_REVERSE_GEOCODE_ENABLED = "origin_reverse_geocode_enabled"
CONF_DESTINATION_REVERSE_GEOCODE_ENABLED = "destination_reverse_geocode_enabled"

DEFAULT_NAME = "Openroute Service Travel Time"

TRAVEL_MODE_BICYCLE = "cycling-regular"
TRAVEL_MODE_ROADBIKE = "cycling-road"
TRAVEL_MODE_MTB = "cycling-mountain"
TRAVEL_MODE_EBIKE = "cycling-electric"
TRAVEL_MODE_CAR = "driving-car"
TRAVEL_MODE_CARHVG = "driving-hvg"
TRAVEL_MODE_PEDESTRIAN = "foot-walking"
TRAVEL_MODE_HIKING = "foot-hiking"
TRAVEL_MODE_WHEELCHAIR = "wheelchair"
TRAVEL_MODE = [
    TRAVEL_MODE_BICYCLE,
    TRAVEL_MODE_ROADBIKE,
    TRAVEL_MODE_MTB,
    TRAVEL_MODE_EBIKE,
    TRAVEL_MODE_CAR,
    TRAVEL_MODE_CARHVG,
    TRAVEL_MODE_PEDESTRIAN,
    TRAVEL_MODE_HIKING,
    TRAVEL_MODE_WHEELCHAIR,
]

ROUTE_MODE_FASTEST = "fastest"
ROUTE_MODE_SHORTEST = "shortest"
ROUTE_MODE = [ROUTE_MODE_FASTEST, ROUTE_MODE_SHORTEST]

ICON_BICYCLE = "mdi:bike"
ICON_ROADBIKE = "mdi:bike"
ICON_MTB = "mdi:bike"
ICON_EBIKE = "mdi:bicycle-electric"
ICON_CAR = "mdi:car"
ICON_CARHVG = "mid:bus"
ICON_PEDESTRIAN = "mdi:walk"
ICON_HIKING = "mdi:hiking"
ICON_WHEELCHAIR = "mdi:wheelchair-accessibility"

ATTR_DURATION = "duration"
ATTR_DISTANCE = "distance"
ATTR_ROUTE = "route"
ATTR_ORIGIN = "origin"
ATTR_DESTINATION = "destination"
ATTR_ORIGIN_NAME = "origin_name"
ATTR_DESTINATION_NAME = "destination_name"

DOMAIN = "open_route_service"