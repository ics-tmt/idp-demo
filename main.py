from fastapi import FastAPI, HTTPException, Query
from calculator import add, subtract, multiply, divide
from weather import WeatherError, fetch_weather

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
def get_weather(
    lat: float,
    lon: float,
    units: str = Query(
        "e", pattern="^(e|m|uk)$", description="Unit system: e (imperial), m (metric), uk (UK)"
    ),
):
    try:
        weather = fetch_weather(lat, lon, units)
    except WeatherError as exc:
        raise HTTPException(status_code=502, detail=str(exc))
    return weather
