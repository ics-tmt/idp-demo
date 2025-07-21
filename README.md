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
pip install fastapi uvicorn pydantic pytest
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

## JIRA Tickets by Story

A new endpoint is available to count JIRA tickets broken down by their associated story.

### API

```bash
curl -X POST "http://127.0.0.1:8000/tickets_by_story" \
  -H "Content-Type: application/json" \
  -d '[{"key":"T1","story":"S1"},{"key":"T2","story":"S1"},{"key":"T3","story":"S2"}]'
```

Example response:

```json
{
  "S1": 2,
  "S2": 1
}
```

## UI

A React UI is provided in the `frontend` directory to visualize the ticket counts.

To run the UI:

```bash
cd frontend
npm install
npm start
```

The app will be available at http://localhost:3000.
