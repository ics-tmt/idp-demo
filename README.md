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

## Jira Tickets Summary

This project provides an API to count Jira tickets broken down by story identifiers.

### Backend

Install dependencies if not already installed:

```bash
pip install fastapi uvicorn pytest
```

Start the API server:

```bash
uvicorn main:app --reload
```

Use the tickets summary endpoint:

```bash
curl -X POST http://127.0.0.1:8000/tickets/summary \
     -H "Content-Type: application/json" \
     -d '[{"id":"JIRA-1","story":"Story-A"},{"id":"JIRA-2","story":"Story-A"}]'
```

Example response:

```json
{"summary":{"Story-A":2}}
```

### UI

A simple React UI is provided under the `frontend` directory to display the tickets summary as a table and bar chart.

To run the UI:

```bash
cd frontend
npm install
npm start
```

This will start the React development server (default port 3000) and proxy API requests to the backend at port 8000.
