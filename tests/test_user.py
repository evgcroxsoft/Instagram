# ________________________________________________________TESTS__________________________________________________________________________________

from models.user import User
from services.test import fake_email, fake_password, fake_phone
from tests.db.conftest import client, session

client_fixture = client
session_fixture = session


def test_register_user(client_fixture, session_fixture):

    user = session_fixture.query(User).filter_by(email=fake_email).first()

    if not user:
        response = client_fixture.post(
            "api/v1/me",
            json={
                "email": fake_email,
                "phone": fake_phone,
                "hashed_password": fake_password,
            },
        )

    assert response.status_code == 201
    data = response.json()
    assert data["email"] == fake_email
    assert data["phone"] == fake_phone

    response = client_fixture.post(
        "api/v1/token", {"username": fake_email, "password": fake_password}
    )
    data = response.json()
    access_token = data["access_token"]
    response = client_fixture.get(
        "api/v1/me", headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
