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

## Jira Story Ticket Counts API and UI

The application provides an endpoint to count Jira tickets broken down by their parent stories and a React-based UI to visualize the results.

### API Endpoint

POST `/jira/story-count`

Request body (JSON):
```json
{
  "tickets": [
    {"id": "T1", "story": "ST-1"},
    {"id": "T2", "story": "ST-2"}
  ]
}
```

Response body (JSON):
```json
{
  "ST-1": 1,
  "ST-2": 1
}
```

### React UI

A simple UI is served at the application root. It allows you to paste a JSON array of tickets, compute counts, and view the results in a table and bar chart.

Start the server and navigate to http://127.0.0.1:8000/ to use the UI.
