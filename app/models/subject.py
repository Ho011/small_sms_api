from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.types import SmallInteger
from app.db.base_class import Base


class Subject(Base):
    id = Column(SmallInteger, primary_key=True, index=True, nullable=False)
    name = Column(String, unique=True, index=True, nullable=False)