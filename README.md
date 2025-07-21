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

## Jira Story Breakdown API

The Jira Story Breakdown API counts how many tickets are associated with each story.

### Endpoint

```
POST /jira/story/count
```

#### Request Body

JSON array of ticket objects. Each ticket must have:
- `key`: the ticket identifier (string)
- `story`: the parent story identifier (string)

Example:
```json
[{"key": "TICKET-1", "story": "STORY-1"},
 {"key": "TICKET-2", "story": "STORY-1"},
 {"key": "TICKET-3", "story": "STORY-2"}]
```

#### Response

JSON object mapping story identifiers to ticket counts:
```json
{"STORY-1": 2, "STORY-2": 1}
```

## UI

A simple React-based UI is provided in `ui/index.html`. It prompts for the tickets JSON, invokes the API, and renders a table and bar chart of the results.

To use the UI, serve the project root (so `/jira/story/count` is reachable), then open `ui/index.html` in your browser.
