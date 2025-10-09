# idp-demo
demorepo

## Scripts

- `calculator.py`: Example calculator script.
- `get_current_time.py`: Script to get the current local date and time.
- `best_of_two.py`: Script to find the maximum (best) of two numbers.
- `main.py`: FastAPI wrapper around the calculator script exposing a `/calculate` endpoint.
- `weather.py`: Helper used by the API to fetch live weather data from weather.com.

## API

Install dependencies:

```bash
pip install fastapi uvicorn requests
```

Start the API server:

```bash
uvicorn main:app --reload
```

Use the API:

```bash
curl "http://127.0.0.1:8000/calculate?operation=add&x=1&y=2"
```

Example response:

```json
{"operation":"add","x":1,"y":2,"result":3}
```

### Weather endpoint

Fetch current conditions (defaults to imperial units):

```bash
curl "http://127.0.0.1:8000/weather?lat=37.77&lon=-122.42"
```

Specify metric units with `units=m`:

```bash
curl "http://127.0.0.1:8000/weather?lat=37.77&lon=-122.42&units=m"
```

Example response:

```json
{
  "location": {
    "name": "San Francisco",
    "city": "San Francisco",
    "state": "California",
    "country": "United States"
  },
  "observation_time": "2024-05-10T16:52:00-07:00",
  "conditions": {
    "phrase": "Partly Cloudy",
    "temperature": 68,
    "feels_like": 68,
    "humidity": 83,
    "wind": {
      "speed": 9,
      "direction_cardinal": "W"
    }
  },
  "sun": {
    "sunrise": "2024-05-10T06:10:00-07:00",
    "sunset": "2024-05-10T20:02:00-07:00"
  },
  "units": "e"
}
```

## Testing

Run tests with pytest:

```bash
pytest
```
