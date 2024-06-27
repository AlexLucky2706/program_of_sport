import pytest
from conftest import client

def test_register():
    response = client.post("/auth/register", json={
        "name": "string",
        "family": "string",
        "age": 1,
        "email": "string",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False
    })
    assert response.status_code == 201