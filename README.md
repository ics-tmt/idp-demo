# idp-demo
demorepo

## Scripts

- `calculator.py`: Example calculator script.
- `get_current_time.py`: Script to get the current local date and time.
- `best_of_two.py`: Script to find the maximum (best) of two numbers.
- `main.py`: FastAPI wrapper around the calculator script exposing a `/calculate` endpoint.

## API

Install Python dependencies:

```bash
pip install -r requirements.txt
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

## Ticket Statistics API

Count JIRA tickets broken down by story via a JSON API.

### Endpoint

```http
POST /count_by_story
Content-Type: application/json

{
  "tickets": [
    { "id": "T1", "story": "Story A" },
    { "id": "T2", "story": "Story B" },
    { "id": "T3", "story": "Story A" }
  ]
}
```

Example successful response:

```json
{ "counts": { "Story A": 2, "Story B": 1 } }
```

## Frontend UI

A React application is provided in the `frontend/` directory. It displays the ticket counts in a table and bar chart.

To run the UI:

```bash
cd frontend
npm install
npm start
```
