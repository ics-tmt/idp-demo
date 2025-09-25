"""Utilities for fetching current weather data from weather.com."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from typing import Any, Dict

import requests

_WEATHER_URL_TEMPLATE = "https://weather.com/weather/today/l/{lat},{lon}"
_DATA_REGEX = re.compile(r'window.__data=JSON.parse\("(.*?)"\);')
_REQUEST_TIMEOUT = 10
_DEFAULT_LANGUAGE = "en-US"

_UNIT_ALIASES = {
    "imperial": "e",
    "metric": "m",
    "e": "e",
    "m": "m",
}

_UNIT_METADATA = {
    "e": {
        "label": "imperial",
        "temperature": "F",
        "windSpeed": "mph",
        "visibility": "mi",
        "pressure": "inHg",
    },
    "m": {
        "label": "metric",
        "temperature": "C",
        "windSpeed": "km/h",
        "visibility": "km",
        "pressure": "hPa",
    },
}


class WeatherDataError(ValueError):
    """Raised when weather data cannot be parsed from the upstream response."""


def get_weather(lat: float, lon: float, units: str = "imperial") -> Dict[str, Any]:
    """Fetch current weather data from weather.com for the provided coordinates."""
    lat = _validate_coordinate(lat, -90, 90, "Latitude")
    lon = _validate_coordinate(lon, -180, 180, "Longitude")

    unit_code = _normalize_units(units)
    unit_meta = _UNIT_METADATA[unit_code]

    response = requests.get(
        _WEATHER_URL_TEMPLATE.format(lat=lat, lon=lon),
        params={"units": unit_code},
        headers={"Accept-Language": _DEFAULT_LANGUAGE, "User-Agent": _user_agent()},
        timeout=_REQUEST_TIMEOUT,
    )
    response.raise_for_status()

    payload = _extract_payload(response.text)
    observation_raw = _extract_observation(payload, unit_code)
    location_raw = _extract_location(payload)

    as_of_iso = _format_timestamp(observation_raw.get("validTimeUtc"))
    observation = {
        "as_of": as_of_iso,
        "phrase": observation_raw.get("wxPhraseLong"),
        "temperature": _format_measure(observation_raw.get("temperature"), unit_meta["temperature"]),
        "feels_like": _format_measure(
            observation_raw.get("temperatureFeelsLike"), unit_meta["temperature"]
        ),
        "humidity": observation_raw.get("relativeHumidity"),
        "wind": {
            "speed": _format_measure(observation_raw.get("windSpeed"), unit_meta["windSpeed"]),
            "direction": observation_raw.get("windDirectionCardinal"),
            "gust": _format_measure(observation_raw.get("windGust"), unit_meta["windSpeed"]),
        },
        "visibility": _format_measure(observation_raw.get("visibility"), unit_meta["visibility"]),
        "pressure": _format_measure(
            _select_pressure(observation_raw, unit_code), unit_meta["pressure"]
        ),
        "uv_index": observation_raw.get("uvIndex"),
        "sunrise": observation_raw.get("sunriseTimeLocal"),
        "sunset": observation_raw.get("sunsetTimeLocal"),
    }

    location = {
        "display_name": location_raw.get("displayName"),
        "city": location_raw.get("city"),
        "region": location_raw.get("adminDistrict"),
        "country": location_raw.get("country"),
        "latitude": location_raw.get("latitude"),
        "longitude": location_raw.get("longitude"),
    }

    return {
        "location": location,
        "units": unit_meta["label"],
        "observation": observation,
    }


def _validate_coordinate(value: Any, lower: float, upper: float, label: str) -> float:
    try:
        numeric_value = float(value)
    except (TypeError, ValueError) as exc:  # pragma: no cover - defensive branch
        raise ValueError(f"{label} must be a number") from exc
    if not (lower <= numeric_value <= upper):
        raise ValueError(f"{label} must be between {lower} and {upper}")
    return numeric_value


def _normalize_units(units: str) -> str:
    if units is None:
        units = "imperial"
    normalized = units.strip().lower()
    if normalized not in _UNIT_ALIASES:
        raise ValueError(
            "Unsupported unit system. Use 'imperial', 'metric', 'e', or 'm'."
        )
    return _UNIT_ALIASES[normalized]


def _extract_payload(html: str) -> Dict[str, Any]:
    match = _DATA_REGEX.search(html)
    if not match:
        raise WeatherDataError("Unable to locate weather payload in weather.com response")
    encoded = match.group(1)
    decoded = bytes(encoded, "utf-8").decode("unicode_escape")
    try:
        return json.loads(decoded)
    except json.JSONDecodeError as exc:  # pragma: no cover - defensive branch
        raise WeatherDataError("Failed to decode weather payload JSON") from exc


def _extract_observation(payload: Dict[str, Any], units: str) -> Dict[str, Any]:
    observations = (
        payload.get("dal", {}).get("getSunV3CurrentObservationsUrlConfig", {})
    )
    for key, entry in observations.items():
        if key.endswith(f"units:{units}"):
            data = entry.get("data")
            if data:
                return data
    raise WeatherDataError("Current observations not found in weather payload")


def _extract_location(payload: Dict[str, Any]) -> Dict[str, Any]:
    locations = payload.get("dal", {}).get("getSunV3LocationPointUrlConfig", {})
    for key, entry in locations.items():
        if key.startswith("geocode:"):
            data = entry.get("data", {})
            if isinstance(data, dict):
                return data.get("location", data)
    return {}


def _format_measure(value: Any, unit: str) -> Dict[str, Any] | None:
    if value is None:
        return None
    return {"value": value, "unit": unit}


def _select_pressure(observation: Dict[str, Any], units: str) -> Any:
    if units == "e":
        return observation.get("pressureAltimeter")
    return observation.get("pressureAltimeter") or observation.get("pressureMeanSeaLevel")


def _format_timestamp(epoch_seconds: Any) -> str | None:
    if not isinstance(epoch_seconds, (int, float)):
        return None
    return datetime.fromtimestamp(epoch_seconds, tz=timezone.utc).isoformat()


def _user_agent() -> str:
    return (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/111.0.0.0 Safari/537.36"
    )
