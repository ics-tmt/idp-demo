# Jira Tickets by Story - Backend

This service provides an API to count Jira tickets grouped by story IDs.

## Requirements

Install dependencies:
```
pip install -r requirements.txt
```

## Running the Service

Start the API server:
```
uvicorn main:app --reload --port 8000
```

## API Endpoint

### POST /tickets/count
- **Description**: Count tickets per story.
- **Request Body**: JSON array of tickets. Each ticket should have:
  - `id` (string): ticket identifier
  - `story_id` (string): associated story identifier
  - `summary` (string, optional): ticket summary
- **Response**: JSON object mapping each `story_id` to its ticket count.

Example:
```bash
curl -X POST http://localhost:8000/tickets/count \
     -H 'Content-Type: application/json' \
     -d '[{"id":"1","story_id":"STORY-1"},{"id":"2","story_id":"STORY-1"}]'
```
```json
{"STORY-1":2}
```

## Tests

Run unit tests with:
```
pytest
```
