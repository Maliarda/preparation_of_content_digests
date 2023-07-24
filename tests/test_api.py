import pytest

from src.main import app


@pytest.mark.asyncio
async def test_get_digest_non_existent_user(client):
    url = app.url_path_for("get_digest")
    response = client.get(
        url,
        params={"user_id": "3422b448-2460-4fd2-9183-8000de6f8343"},
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


@pytest.mark.asyncio
async def test_get_digest_exist_user(client):
    url = app.url_path_for("get_digest")
    response = client.get(
        url,
        params={"user_id": "a29e7712-c6aa-4833-bfd0-79522cd5c3ae"},
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Digest not found"}


@pytest.mark.asyncio
async def test_create_digest_no_posts(client):
    url = app.url_path_for("create_digest")
    response = client.post(
        url,
        params={
            "user_id": "a29e7712-c6aa-4833-bfd0-79522cd5c3ae",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "user_id": "a29e7712-c6aa-4833-bfd0-79522cd5c3ae",
        "message": "No posts for digest",
    }
