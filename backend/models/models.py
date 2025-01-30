from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(50), nullable=False)
    user_email = Column(String(100), nullable=False, unique=True)
    user_password = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.now())

class Note(Base):
    __tablename__ = 'notes'

    note_id = Column(Integer, primary_key=True, index=True)
    note_name = Column(String(50), nullable=False)
    note_content = Column(String(200), nullable=False)
    user_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())