# idp-demo
demorepo

## Scripts

- `calculator.py`: Example calculator script.
- `get_current_time.py`: Script to get the current local date and time.
- `best_of_two.py`: Script to find the maximum (best) of two numbers.
- `main.py`: FastAPI wrapper around the calculator script exposing `/calculate` and `/jira/count` endpoints.
- `jira_counter.py`: Module providing functionality to count Jira tickets by story.

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

### Jira Tickets Count

Use the Jira tickets count API endpoint:

```bash
curl -X POST "http://127.0.0.1:8000/jira/count" -H "Content-Type: application/json" -d '[{"id":"T1","story_id":"S1"},{"id":"T2","story_id":"S1"},{"id":"T3","story_id":"S2"}]'
```

Example response:

```json
{"S1":2,"S2":1}
```

## Frontend

A React application under `frontend/` displays the Jira ticket counts in a table and bar chart.

In the `frontend/` directory, install dependencies and start the development server:

```bash
npm install
npm start
```

## Testing

Run tests with pytest:

```bash
pytest
```
