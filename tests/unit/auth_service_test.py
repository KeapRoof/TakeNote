import pytest
from unittest.mock import AsyncMock
from fastapi import HTTPException
from services.auth_service import (
    hash_password, verify_password, create_access_token, verify_token,
    get_current_user, create_user, authenticate_user
)
from models.models import User
import jwt


def test_hash_and_verify_password():
    password = "testpassword"
    hashed = hash_password(password)
    assert hashed != password  # Le mot de passe doit être hashé
    assert verify_password(password, hashed)  # Vérification réussie
    assert not verify_password("wrongpassword", hashed)  # Mauvaise vérification échoue

def test_create_access_token():
    data = {"sub": "123"}
    token = create_access_token(data)
    assert isinstance(token, str)  # Le token doit être une chaîne

def test_verify_token_valid():
    data = {"sub": "123"}
    token = create_access_token(data)
    user_id = verify_token(token)
    assert user_id == 123

def test_verify_token_invalid():
    with pytest.raises(HTTPException) as exc_info:
        verify_token("invalidtoken")
    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Token invalide"

@pytest.mark.asyncio
async def test_get_current_user_valid():
    mock_db = AsyncMock()
    user = User(user_id=1, user_email="test@exampl.com", user_name="testuser")
    mock_db.execute.return_value.scalar_one_or_none.return_value =  user

    token = create_access_token({"sub": "1"})
    current_user = await get_current_user(token=token, db=mock_db)

    assert current_user == user

@pytest.mark.asyncio
async def test_get_current_user_not_found():
    mock_db = AsyncMock()
    mock_db.execute.return_value.scalar_one_or_none.return_value = None

    token = create_access_token({"sub": "1"})
    with pytest.raises(HTTPException) as exc_info:
        await get_current_user(token=token, db=mock_db)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Utilisateur non trouvé"

@pytest.mark.asyncio
async def test_authenticate_user_valid():
    mock_db = AsyncMock()
    hashed_password = hash_password("testpassword")
    user = User(user_id=1, user_email="test@example.com", user_password=hashed_password, user_name="nametest")
    mock_db.execute.return_value.scalar_one_or_none.return_value = user

    authenticated_user = await authenticate_user(
        email="test@example.com",
        password="testpassword",
        db=mock_db
    )

    assert authenticated_user == user

@pytest.mark.asyncio
async def test_authenticate_user_invalid():
    mock_db = AsyncMock()
    mock_db.execute.return_value.scalar_one_or_none.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        await authenticate_user(
            email="test@example.com",
            password="wrongpassword",
            db=mock_db
        )

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Email ou mot de passe incorrect"

@pytest.mark.asyncio
async def test_create_user_success():
    mock_db = AsyncMock()
    mock_db.execute.return_value.scalar_one_or_none.return_value = None # Pas d'utilisateur existant

    new_user = await create_user(
        user_email="test@example.com",
        username="username",
        password="password",
        db=mock_db
    )

    assert new_user.user_email == "test@example.com"
    assert new_user.user_name == "username"
    mock_db.commit.assert_called_once()

@pytest.mark.asyncio
async def test_create_user_email_exists():
    mock_db = AsyncMock()
    mock_db.execute.return_value.scalar_one_or_none.side_effect = [
        User(user_email="test@example.com"),  # Email existant
        None
    ]

    with pytest.raises(HTTPException) as exc_info:
        await create_user(
            user_email="test@example.com",
            username="testuser",
            password="testpassword",
            db=mock_db
        )

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Email déjà utilisé"
