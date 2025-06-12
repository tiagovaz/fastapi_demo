from sqlmodel import create_engine, Session, SQLModel
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Create tables on startup
def on_startup():
    SQLModel.metadata.create_all(engine)

# Dependency to get a session
def get_session():
    with Session(engine) as session:
        yield session
