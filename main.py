from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from calculator import add, subtract, multiply, divide
from jira_metrics import JiraClient

app = FastAPI()

# enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


@app.get("/jira/story-subtasks")
def story_subtasks(project_key: str):
    """
    Get the number of subtasks broken out for each story in a project.
    """
    try:
        client = JiraClient()
        return client.count_subtasks_by_story(project_key)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception:
        raise HTTPException(status_code=502, detail="Error fetching data from JIRA")
