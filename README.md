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

Add the Jira ticket analysis endpoint:

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
     -H 'Content-Type: application/json' \
     -d '{"stories":[{"id":"S1","tickets":["JIRA-1","JIRA-2"]}]}'
```

Example response:

```json
{
  "results":[{"id":"S1","count":2}]
}
```

Example response:

```json
{"operation":"add","x":1,"y":2,"result":3}
```

## Testing

Run tests with pytest:

```bash
pytest

# UI

Open `ui/index.html` in a browser to load a simple React-based UI for pasting story data, viewing a table of counts, and a bar chart.
```
