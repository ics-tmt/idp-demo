import json

import pytest

import weather


def _build_html(payload):
    encoded = json.dumps(payload)
    encoded = encoded.replace("\\", "\\\\").replace('"', '\\"')
    return f"<html><script>window.__data=JSON.parse(\"{encoded}\");</script></html>"


def test_get_weather_success(monkeypatch):
    payload = {
        "dal": {
            "getSunV3CurrentObservationsUrlConfig": {
                "geocode:12.34,56.78;language:en-US;units:e": {
                    "status": 200,
                    "data": {
                        "validTimeUtc": 1,
                        "wxPhraseLong": "Partly Cloudy",
                        "temperature": 70,
                        "temperatureFeelsLike": 68,
                        "relativeHumidity": 55,
                        "windSpeed": 12,
                        "windDirectionCardinal": "NW",
                        "windGust": 15,
                        "visibility": 10,
                        "pressureAltimeter": 29.92,
                        "uvIndex": 3,
                        "sunriseTimeLocal": "2025-09-25T06:00:00-0700",
                        "sunsetTimeLocal": "2025-09-25T18:30:00-0700",
                    },
                }
            },
            "getSunV3LocationPointUrlConfig": {
                "geocode:12.34,56.78;language:en-US": {
                    "data": {
                        "location": {
                            "displayName": "Sample City",
                            "city": "Sample",
                            "adminDistrict": "Region",
                            "country": "Country",
                            "latitude": 12.34,
                            "longitude": 56.78,
                        }
                    }
                }
            },
        }
    }

    html = _build_html(payload)

    class FakeResponse:
        status_code = 200
        text = html

        def raise_for_status(self):
            return None

    def fake_get(url, params=None, headers=None, timeout=None):
        assert params == {"units": "e"}
        return FakeResponse()

    monkeypatch.setattr(weather.requests, "get", fake_get)
    result = weather.get_weather(12.34, 56.78, units="imperial")
    assert result["units"] == "imperial"
    assert result["location"]["display_name"] == "Sample City"
    assert result["observation"]["temperature"] == {"value": 70, "unit": "F"}
    assert result["observation"]["wind"]["speed"] == {"value": 12, "unit": "mph"}


def test_get_weather_invalid_units():
    with pytest.raises(ValueError):
        weather.get_weather(0, 0, units="kelvin")


def test_get_weather_upstream_error(monkeypatch):
    html = "<html></html>"

    class FakeResponse:
        status_code = 200
        text = html

        def raise_for_status(self):
            return None

    def fake_get(url, params=None, headers=None, timeout=None):
        return FakeResponse()

    monkeypatch.setattr(weather.requests, "get", fake_get)
    with pytest.raises(weather.WeatherDataError):
        weather.get_weather(0, 0)
