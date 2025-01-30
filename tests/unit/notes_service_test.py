import pytest
from unittest.mock import AsyncMock
from services.notes_service import (
    create_note_service,
    get_notes_service,
    update_note_service,
    delete_note_service,
    get_note_service
)
from models.models import Note
from schemas.schemas import NoteUpdateRequest


@pytest.mark.asyncio
async def test_create_note_service():
    mock_db = AsyncMock()
    mock_db.execute.return_value = []
    user_id = 1
    new_note = await create_note_service(user_id=user_id, db=mock_db)
    assert new_note.note_name == "Nouvelle Note"
    assert new_note.note_content == "Test content"
    assert new_note.user_id == user_id
    mock_db.add.assert_called_once_with(new_note)
    mock_db.commit.assert_called_once()


@pytest.mark.asyncio
async def test_get_notes_service():
    mock_db = AsyncMock()
    mock_db.execute.return_value.scalars.return_value.all.return_value = [
        Note(note_id=1, note_name="Note 1", note_content="Content 1", user_id=1),
        Note(note_id=2, note_name="Note 2", note_content="Content 2", user_id=1)
    ]
    user_id = 1
    notes = await get_notes_service(user_id=user_id, db=mock_db)
    assert len(notes) == 2
    assert notes[0].note_name == "Note 1"
    assert notes[1].note_name == "Note 2"



@pytest.mark.asyncio
async def test_update_note_service():
    mock_db = AsyncMock()
    mock_db.execute.return_value.scalars.return_value.first.return_value = Note(note_id=1, note_name="Old Note", note_content="Old content", user_id=1)
    note_update = NoteUpdateRequest(note_name="Updated Note", note_content="Updated content")
    user_id = 1
    note_id = 1
    mock_db.execute.return_value.scalar_one_or_none.return_value = Note(note_id=note_id, note_name=note_update.note_name, note_content=note_update.note_content, user_id=user_id)
    updated_note = await update_note_service(note_id, user_id, note_update, mock_db)
    assert updated_note.note_name == "Updated Note"
    assert updated_note.note_content == "Updated content"
    mock_db.commit.assert_called_once()


@pytest.mark.asyncio
async def test_delete_note_service():
    mock_db = AsyncMock()
    mock_db.execute.return_value.scalars.return_value.first.return_value = Note(note_id=1, note_name="Note to Delete", note_content="Content", user_id=1)
    user_id = 1
    note_id = 1
    deleted_note = await delete_note_service(note_id=note_id, user_id=user_id, db=mock_db)
    assert deleted_note.note_id == note_id
    mock_db.commit.assert_called_once()


@pytest.mark.asyncio
async def test_delete_note_service_not_found():
    mock_db = AsyncMock()
    mock_db.execute.return_value.scalars.return_value.first.return_value = None
    user_id = 1
    note_id = 1
    deleted_note = await delete_note_service(note_id=note_id, user_id=user_id, db=mock_db)
    assert deleted_note is None
    mock_db.delete.assert_not_called()
    mock_db.commit.assert_not_called()


@pytest.mark.asyncio
async def test_get_note_service():
    mock_db = AsyncMock()
    mock_db.execute.return_value.scalar_one_or_none.return_value = Note(note_id=1, note_name="Note 1", note_content="Content", user_id=1)
    user_id = 1
    note_id = 1
    note = await get_note_service(note_id=note_id, user_id=user_id, db=mock_db)
    assert note.note_name == "Note 1"
    assert note.note_content == "Content"
    assert note.user_id == user_id


@pytest.mark.asyncio
async def test_get_note_service_not_found():
    mock_db = AsyncMock()
    mock_db.execute.return_value.scalar_one_or_none.return_value = None
    user_id = 1
    note_id = 1
    note = await get_note_service(note_id=note_id, user_id=user_id, db=mock_db)
    assert note is None
