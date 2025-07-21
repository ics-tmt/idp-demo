# idp-demo
demorepo

## Scripts

- `calculator.py`: Example calculator script.
- `get_current_time.py`: Script to get the current local date and time.
- `best_of_two.py`: Script to find the maximum (best) of two numbers.
- `main.py`: FastAPI wrapper around the calculator script exposing a `/calculate` endpoint.

## API

Install dependencies:

```bash
pip install fastapi uvicorn
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

## Testing

Run tests with pytest:

```bash
pytest
```

## Jira Tickets by Story Service

This service provides an endpoint to count JIRA tickets broken down by story names.

### API Endpoint

POST `/tickets_by_story`

Request JSON body:
```json
{
  "tickets": [
    {"key": "JIRA-1", "story": "Story A"},
    {"key": "JIRA-2", "story": "Story B"}
  ]
}
```

Response JSON:
```json
{ "counts": { "Story A": 1, "Story B": 1 } }
```

### React UI

Open `frontend/index.html` in a browser while the API server is running (e.g., at http://localhost:8000).
Paste an array of ticket objects into the textarea and click **Submit** to view a table and bar chart of ticket counts by story.
