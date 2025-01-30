from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.schemas import UserCreate, LoginRequest
from services.auth_service import authenticate_user, create_access_token, create_user
from database import get_db

router = APIRouter()

# Route pour login
@router.post("/api/login")
async def login_to_note(credentials: LoginRequest, db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(credentials.email, credentials.password, db)
    access_token = create_access_token(data={"sub": str(user.user_id)})
    return {"access_token": access_token, "token_type": "bearer"}

# Route pour créer un utilisateur
@router.post("/api/signup")
async def signup(user: UserCreate, db: AsyncSession = Depends(get_db)):
    # Appeler la fonction de création de compte dans le service
    new_user = await create_user(user.email, user.username, user.password, db)

    # Retourner une réponse indiquant que l'utilisateur a été créé
    return {"message": "Utilisateur créé avec succès", "user": {"email": new_user.user_email}}