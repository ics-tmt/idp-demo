import json
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import requests


class WeatherError(Exception):
    """Raised when weather data cannot be retrieved or parsed."""


_DATA_PREFIX = 'window.__data=JSON.parse("'
_DATA_SUFFIX = '"); window.__i18n'


@dataclass
class _Observation:
    data: Dict[str, Any]
    units: str
    geocode: Optional[Tuple[float, float]]


def fetch_weather(latitude: float, longitude: float, units: str = "e") -> Dict[str, Any]:
    """
    Fetch weather information from weather.com for the provided coordinates.

    :param latitude: Latitude component of the desired location.
    :param longitude: Longitude component of the desired location.
    :param units: Unit system. Supported values: "e" (imperial), "m" (metric), "uk" (UK).
    :returns: Dictionary with the parsed weather details.
    :raises WeatherError: If the data cannot be fetched or parsed.
    """
    units = units.lower()
    if units not in {"e", "m", "uk"}:
        raise WeatherError(f"Unsupported units: {units}")

    url = f"https://weather.com/weather/today/l/{latitude},{longitude}"
    params = {"unit": units}
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/123.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise WeatherError("Failed to fetch weather data from weather.com") from exc

    try:
        return parse_weather_html(response.text)
    except WeatherError:
        raise
    except Exception as exc:  # pragma: no cover - safety net
        raise WeatherError("Failed to parse weather data from weather.com") from exc


def parse_weather_html(html: str) -> Dict[str, Any]:
    """
    Parse the weather.com HTML payload and extract relevant weather information.

    :param html: Raw HTML returned by weather.com.
    :returns: Dictionary containing structured weather information.
    :raises WeatherError: If the expected data cannot be located.
    """
    payload = _extract_weather_payload(html)
    observation = _extract_observation(payload)
    location = _extract_location(payload, observation.geocode)

    obs_data = observation.data
    location = location or {}

    return {
        "location": {
            "name": location.get("displayName"),
            "city": location.get("city"),
            "state": location.get("adminDistrict"),
            "country": location.get("country"),
            "latitude": location.get("latitude"),
            "longitude": location.get("longitude"),
        },
        "observation_time": obs_data.get("validTimeLocal"),
        "conditions": {
            "phrase": obs_data.get("wxPhraseLong") or obs_data.get("wxPhraseShort"),
            "temperature": obs_data.get("temperature"),
            "feels_like": obs_data.get("temperatureFeelsLike"),
            "dew_point": obs_data.get("temperatureDewPoint"),
            "humidity": obs_data.get("relativeHumidity"),
            "wind": {
                "speed": obs_data.get("windSpeed"),
                "gust": obs_data.get("windGust"),
                "direction": obs_data.get("windDirection"),
                "direction_cardinal": obs_data.get("windDirectionCardinal"),
            },
            "visibility": obs_data.get("visibility"),
            "pressure": obs_data.get("pressureMeanSeaLevel"),
            "uv_index": obs_data.get("uvIndex"),
            "uv_description": obs_data.get("uvDescription"),
        },
        "sun": {
            "sunrise": obs_data.get("sunriseTimeLocal"),
            "sunset": obs_data.get("sunsetTimeLocal"),
        },
        "units": observation.units,
    }


def _extract_weather_payload(html: str) -> Dict[str, Any]:
    if _DATA_PREFIX not in html or _DATA_SUFFIX not in html:
        raise WeatherError("Could not locate weather data in the HTML payload")

    start_index = html.index(_DATA_PREFIX) + len(_DATA_PREFIX)
    end_index = html.index(_DATA_SUFFIX, start_index)
    raw_payload = html[start_index:end_index]

    try:
        decoded_payload = raw_payload.encode("utf-8").decode("unicode_escape")
        return json.loads(decoded_payload)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise WeatherError("Unable to decode weather data payload") from exc


def _extract_observation(payload: Dict[str, Any]) -> _Observation:
    obs_config = payload.get("dal", {}).get("getSunV3CurrentObservationsUrlConfig") or {}
    for key, record in obs_config.items():
        data = record.get("data")
        if not data:
            continue

        units = "e"
        geocode = None
        if ";units:" in key:
            units = key.split(";units:")[-1]
        if key.startswith("geocode:"):
            try:
                geo_part = key.split(";", 1)[0].split(":", 1)[1]
                lat_str, lon_str = geo_part.split(",", 1)
                geocode = (float(lat_str), float(lon_str))
            except (ValueError, IndexError):
                geocode = None

        return _Observation(data=data, units=units, geocode=geocode)

    raise WeatherError("Weather observation data is unavailable")


def _extract_location(payload: Dict[str, Any], geocode: Optional[Tuple[float, float]]) -> Optional[Dict[str, Any]]:
    location_config = payload.get("dal", {}).get("getSunV3LocationPointUrlConfig") or {}
    if not location_config:
        return None

    # Attempt direct geocode match first.
    if geocode is not None:
        lat, lon = geocode
        best_match = None
        best_score = float("inf")
        for record in location_config.values():
            loc = record.get("data", {}).get("location")
            if not loc:
                continue
            loc_lat = loc.get("latitude")
            loc_lon = loc.get("longitude")
            if loc_lat is None or loc_lon is None:
                continue
            score = abs(loc_lat - lat) + abs(loc_lon - lon)
            if score < best_score:
                best_match = loc
                best_score = score
        if best_match:
            return best_match

    # Fall back to the first location entry.
    for record in location_config.values():
        loc = record.get("data", {}).get("location")
        if loc:
            return loc

    return None

