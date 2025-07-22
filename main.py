from fastapi import FastAPI, HTTPException
from calculator import add, subtract, multiply, divide
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount UI static files (React app)
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

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

# Include JIRA statistics endpoints
from api.jira import router as jira_router
app.include_router(jira_router, prefix="/jira")
