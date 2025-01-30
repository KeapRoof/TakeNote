from fastapi import HTTPException, status
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import jwt
from datetime import datetime, timedelta
from models.models import User
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from database import get_db


SECRET_KEY = "my_secret_key_12345@development"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    user_id = verify_token(token)
    result = await db.execute(select(User).where(User.user_id == user_id))
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur non trouvé")
    return user

# Hachage du mot de passe
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

async def create_user(user_email: str, username: str, password: str, db: AsyncSession):
    # Vérifier si l'email existe déjà
    result_email = await db.execute(select(User).where(User.user_email == user_email))
    existing_user_email = result_email.scalar_one_or_none()

    if existing_user_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email déjà utilisé")

    # Vérifier si le nom d'utilisateur existe déjà
    result_username = await db.execute(select(User).where(User.user_name == username))
    existing_user_username = result_username.scalar_one_or_none()

    if existing_user_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nom d'utilisateur déjà pris")

    # Hachage du mot de passe
    hashed_password = hash_password(password)

    # Création du nouvel utilisateur
    new_user = User(user_name=username, user_email=user_email, user_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user

# Vérification du mot de passe
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Créer un token d'accès JWT
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Vérifier le token JWT
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return int(payload.get("sub"))
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expiré")
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalide")

# Authentifier un utilisateur
async def authenticate_user(email: str, password: str, db: AsyncSession):
    result = await db.execute(select(User).where(User.user_email == email))
    user = result.scalar_one_or_none()
    if user is None or not verify_password(password, user.user_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email ou mot de passe incorrect")
    return user

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    user_id = verify_token(token)
    result = await db.execute(select(User).where(User.user_id == user_id))
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur non trouvé")
    return user
