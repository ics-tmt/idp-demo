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

### Jira Ticket Count Service

#### API

Count Jira tickets broken down by stories.

```bash
curl -X POST http://127.0.0.1:8000/jira/story_counts \
     -H "Content-Type: application/json" \
     -d '[{"id":"T1","story":"S1"},{"id":"T2","story":"S1"},{"id":"T3","story":"S2"}]'
```

Example response:

```json
{"S1":2,"S2":1}
```

## Testing

Run tests with pytest:

```bash
pytest
```

## Frontend UI

A React-based UI is provided in the `frontend/` directory. To run:

```bash
cd frontend
npm install
npm start
```

The app will be available at http://localhost:3000 and will interact with the Jira story counts API at http://localhost:8000/jira/story_counts.
