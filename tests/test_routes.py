import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the API' in response.data

def test_invalid_endpoint(client):
    response = client.get('/invalid_endpoint')
    assert response.status_code == 404
    assert b'Not Found' in response.data

def test_add_task(client):
    response = client.post("/", data={"task": "test task"})
    assert b"test task" in response.data

