from sqlmodel import SQLModel, Field
from typing import Optional

# SQLModel data model
# We could also use SQLAlchemy directly, but this looks simpler
# for ORM (Object-Relational Mapping)
class TodoItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) # will auto-increment
    title: str
    completed: bool = False
