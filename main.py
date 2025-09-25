import requests
from fastapi import FastAPI, HTTPException

from calculator import add, subtract, multiply, divide
from weather import WeatherDataError, get_weather

app = FastAPI()

@app.get("/calculate")
def calculate(operation: str, x: float, y: float):
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }
    if operation not in operations:
        raise HTTPException(status_code=400, detail=f"Invalid operation: {operation}")
    func = operations[operation]
    try:
        result = func(x, y)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"operation": operation, "x": x, "y": y, "result": result}


@app.get("/weather")
def weather(lat: float, lon: float, units: str = "imperial"):
    try:
        return get_weather(lat, lon, units)
    except WeatherDataError as exc:
        raise HTTPException(status_code=502, detail=str(exc))
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except requests.RequestException as exc:  # pragma: no cover - network failure
        raise HTTPException(status_code=502, detail="Failed to reach weather.com") from exc
