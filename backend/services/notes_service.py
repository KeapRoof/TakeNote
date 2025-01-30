from datetime import datetime

from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.models import Note, User
from schemas.schemas import NoteUpdateRequest
from services.auth_service import verify_token

# Créer une nouvelle note
async def create_note_service(user_id: int, db: AsyncSession):
    result = await db.execute(select(Note).filter(Note.user_id == user_id))
    new_note = Note(note_name="Nouvelle Note", note_content="", user_id=user_id) 
    db.add(new_note)
    await db.commit()
    return new_note

# Obtenir toutes les notes d'un utilisateur
async def get_notes_service(user_id: int, db: AsyncSession):
    result = await db.execute(select(Note).where(Note.user_id == user_id))
    res = result.scalars()
    return res.all()

# Mettre à jour une note
async def update_note_service(note_id: int, user_id: int, note:NoteUpdateRequest, db: AsyncSession):
    query = select(Note).filter(Note.note_id == note_id, Note.user_id == user_id)
    result = await db.execute(query)
    res = result.scalars()
    note_db = res.first()

    if note_db is None:
        return None

    # Mise à jour explicite des champs nécessaires
    update_stmt = (
        update(Note)
        .where(Note.note_id == note_id, Note.user_id == user_id)
        .values(
            note_name=note.note_name,
            note_content=note.note_content,
            updated_at=datetime.utcnow()  # Mise à jour de updated_at
        )
        .execution_options(synchronize_session="fetch")
    )

    await db.execute(update_stmt)
    await db.commit()

    # Retourner la version mise à jour de la note
    return await get_note_service(note_id, user_id, db)

# Supprimer une note
async def delete_note_service(note_id: int, user_id: int, db: AsyncSession):
    result = await db.execute(select(Note).filter(Note.note_id == note_id, Note.user_id == user_id))
    res = result.scalars()
    note = res.first()
    if note:
        await db.delete(note)
        await db.commit()
        return note
    return None

# Obtenir une note par son ID
async def get_note_service(note_id: int, user_id:int, db: AsyncSession):
    result = await db.execute(select(Note).where(Note.note_id == note_id, Note.user_id == user_id))
    note = result.scalar_one_or_none()
    if note is None:
        return None
    return note
