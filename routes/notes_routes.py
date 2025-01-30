from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.schemas import NotesResponse
from services.notes_service import *
from services.auth_service import get_current_user
from models.models import User
from database import get_db

router = APIRouter()

# Route pour obtenir les notes de l'utilisateur
@router.get("/api/notes", response_model=list[NotesResponse])
async def get_notes(current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    notes = await get_notes_service(current_user.user_id, db)
    return notes

# Route pour créer une note
@router.post("/api/note")
async def create_note(current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    note = await create_note_service(current_user.user_id, db)
    return note

# Route pour mettre à jour une note
@router.put("/api/note/{note_id}")
async def update_note(note_id: int, note: NoteUpdateRequest, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    updated_note = await update_note_service(note_id, current_user.user_id,note, db)
    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note

# Route pour supprimer une note
@router.delete("/api/note/{note_id}")
async def delete_note(note_id: int, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    deleted_note = await delete_note_service(note_id, current_user.user_id, db)
    if not deleted_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}

@router.get("/api/note/{note_id}")
async def get_note(note_id: int, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    note = await get_note_service(note_id, current_user.user_id, db)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note