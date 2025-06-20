import pytest
import pytest_asyncio
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from app.main import app

@pytest_asyncio.fixture
async def client():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            yield ac

@pytest.mark.asyncio
async def test_create_user(client):
    user_data = {
        "firstname": "Test",
        "lastname": "User",
        "email": "testuser@example.com",
        "birthdate": "1990-01-01",
        "city": "TestCity",
        "postal_code": "12345",
        "password": "testpassword"
    }
    response = await client.post("/api/users", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "testuser@example.com"

@pytest.mark.asyncio
async def test_list_users(client):
    response = await client.get("/api/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

@pytest.mark.asyncio
async def test_login(client):
    login_data = {
        "email": "testuser@example.com",
        "password": "testpassword"
    }
    response = await client.post("/api/login", json=login_data)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data or "token" in data

@pytest.mark.asyncio
async def test_delete_user_unauthorized(client):
    response = await client.delete("/api/users/1")
    assert response.status_code == 401
