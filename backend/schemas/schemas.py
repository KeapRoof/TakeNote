from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: str
    password: str
    username: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class LoginRequest(BaseModel):
    email: str
    password: str

class NotesResponse(BaseModel):
    note_id: int
    note_name: str
    note_content: str
    created_at: datetime

    class Config:
        orm_mode = True

    class Config:
        orm_mode = True

class NoteUpdateRequest(BaseModel):
    note_name: str
    note_content: str