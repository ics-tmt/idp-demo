import json

import pytest

from weather import WeatherError, parse_weather_html, fetch_weather


def _build_sample_html(payload: dict) -> str:
    raw_json = json.dumps(payload)
    escaped_json = raw_json.replace("\\", "\\\\").replace('"', '\\"')
    return (
        f'<html><body><script>window.__data=JSON.parse("{escaped_json}"); '
        "window.__i18n=window.__data.i18n.i18n;</script></body></html>"
    )


def test_parse_weather_html_extracts_expected_fields():
    payload = {
        "page": {},
        "dal": {
            "getSunV3CurrentObservationsUrlConfig": {
                "geocode:37.76,-122.42;language:en-US;units:e": {
                    "data": {
                        "validTimeLocal": "2024-05-10T16:52:00-07:00",
                        "wxPhraseLong": "Partly Cloudy",
                        "wxPhraseShort": "Partly Cloudy",
                        "temperature": 68,
                        "temperatureFeelsLike": 68,
                        "temperatureDewPoint": 57,
                        "relativeHumidity": 83,
                        "windSpeed": 9,
                        "windGust": 15,
                        "windDirection": 270,
                        "windDirectionCardinal": "W",
                        "visibility": 10,
                        "pressureMeanSeaLevel": 30.12,
                        "uvIndex": 4,
                        "uvDescription": "Moderate",
                        "sunriseTimeLocal": "2024-05-10T06:10:00-07:00",
                        "sunsetTimeLocal": "2024-05-10T20:02:00-07:00",
                    }
                }
            },
            "getSunV3LocationPointUrlConfig": {
                "geocode:37.77,-122.42;language:en-US": {
                    "data": {
                        "location": {
                            "displayName": "San Francisco",
                            "city": "San Francisco",
                            "adminDistrict": "California",
                            "country": "United States",
                            "latitude": 37.757,
                            "longitude": -122.419,
                        }
                    }
                }
            },
        },
    }
    html = _build_sample_html(payload)

    result = parse_weather_html(html)

    assert result["location"]["name"] == "San Francisco"
    assert result["conditions"]["temperature"] == 68
    assert result["conditions"]["wind"]["direction_cardinal"] == "W"
    assert result["sun"]["sunrise"] == "2024-05-10T06:10:00-07:00"
    assert result["units"] == "e"


def test_fetch_weather_rejects_unsupported_units():
    with pytest.raises(WeatherError):
        fetch_weather(0.0, 0.0, units="unsupported")

