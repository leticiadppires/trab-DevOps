import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_root_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_root_response_json():
    response = client.get("/")
    assert response.json() == {"message": "Hello World"}


def test_root_content_type():
    response = client.get("/")
    assert "application/json" in response.headers["content-type"]


def test_root_has_message_key():
    response = client.get("/")
    assert "message" in response.json()


def test_root_message_value():
    response = client.get("/")
    assert response.json()["message"] == "Hello World"