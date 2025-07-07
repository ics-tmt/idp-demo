# idp-demo
demorepo

## Scripts

- `calculator.py`: Example calculator script.
- `get_current_time.py`: Script to get the current local date and time.
- `prime.py`: Script to check if a number is prime.
- `best_of_two.py`: Script to find the maximum (best) of two numbers.
- `main.py`: FastAPI wrapper around the calculator and prime scripts exposing `/calculate` and `/is_prime` endpoints.

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
curl "http://127.0.0.1:8000/is_prime?n=17"
```

Example response:

```json
{"operation":"add","x":1,"y":2,"result":3}
```

```json
{"n":17,"is_prime":true}
```

## Testing

Run tests with pytest:

```bash
pytest
```
