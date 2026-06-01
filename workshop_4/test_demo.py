import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_first():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 0.3 # เวลาจริง ได้มากกว่า 100 ms


def test_second():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.json().get("username") == "Bret" # เซฟกว่าการใช้ ["username"]
    assert response.json().get("address").get("city") == "Gwenborough"

def test_third():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404


