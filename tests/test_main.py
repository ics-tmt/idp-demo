from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_add_operation():
    response = client.get(
        "/calculate", params={"operation": "add", "x": 1, "y": 2}
    )
    assert response.status_code == 200
    assert response.json() == {"operation": "add", "x": 1.0, "y": 2.0, "result": 3.0}


def test_subtract_operation():
    response = client.get(
        "/calculate", params={"operation": "subtract", "x": 5, "y": 3}
    )
    assert response.status_code == 200
    assert response.json() == {"operation": "subtract", "x": 5.0, "y": 3.0, "result": 2.0}


def test_multiply_operation():
    response = client.get(
        "/calculate", params={"operation": "multiply", "x": 3, "y": 4}
    )
    assert response.status_code == 200
    assert response.json() == {"operation": "multiply", "x": 3.0, "y": 4.0, "result": 12.0}


def test_divide_operation():
    response = client.get(
        "/calculate", params={"operation": "divide", "x": 10, "y": 2}
    )
    assert response.status_code == 200
    assert response.json() == {"operation": "divide", "x": 10.0, "y": 2.0, "result": 5.0}


def test_invalid_operation():
    response = client.get(
        "/calculate", params={"operation": "foo", "x": 1, "y": 2}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid operation: foo"


def test_divide_by_zero_operation():
    response = client.get(
        "/calculate", params={"operation": "divide", "x": 1, "y": 0}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Cannot divide by zero"


def test_is_prime_true():
    response = client.get("/is_prime", params={"n": 17})
    assert response.status_code == 200
    assert response.json() == {"n": 17, "is_prime": True}


def test_is_prime_false():
    response = client.get("/is_prime", params={"n": 18})
    assert response.status_code == 200
    assert response.json() == {"n": 18, "is_prime": False}