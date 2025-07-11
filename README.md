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
pip install fastapi uvicorn requests python-dotenv pytest
```

### Backend

Start the API server (ensure you have copied `.env.example` to `.env` and filled in your Jira credentials):

```bash
cp .env.example .env
uvicorn main:app --reload
```

#### Jira Summary API Endpoint

```bash
curl "http://127.0.0.1:8000/jira-summary?jql=project=MYPROJECT"
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
