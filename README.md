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

## Jira Tickets by Story API and UI

### Configuration

The Jira integration requires the following environment variables:

```bash
export JIRA_SERVER="https://your-jira-instance"
export JIRA_USERNAME="your-username"
export JIRA_API_TOKEN="your-api-token"
export JIRA_PROJECT_KEY="PROJECTKEY"
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the API server

```bash
uvicorn main:app --reload
```

### Access the API

The endpoint to fetch ticket counts by story is:

```
GET /jira/tickets_by_story
```

### UI

Once the server is running, open your browser to `http://127.0.0.1:8000/` to view the React-based UI showing a table and bar chart of ticket counts by story.
