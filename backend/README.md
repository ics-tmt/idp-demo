# Jira Story Count API

This service provides an API to count the number of JIRA story tickets by their parent ticket.

## API Endpoint

### POST /story_counts

Request Body (JSON array of tickets):
```json
[
  {"key": "ABC-1", "issue_type": "Story", "parent": "EPIC-1"},
  {"key": "ABC-2", "issue_type": "Task", "parent": "EPIC-1"}
]
```

Response (JSON object mapping parent key to story count):
```json
{ "EPIC-1": 1 }
```

## Installation and Running

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## Testing

```bash
cd backend
pytest
```
```
