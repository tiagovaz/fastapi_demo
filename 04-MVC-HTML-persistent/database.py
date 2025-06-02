from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the database URL from the environment, otherwise use sqlite test.db
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Create tables on startup
def on_startup():
    SQLModel.metadata.create_all(engine)

# Dependency to get a session
def get_session():
    with Session(engine) as session:
        yield session

###### .env file sample ###########
## PostgreSQL database URL
#DATABASE_URL_POSTGRESQL=postgresql+psycopg2://user:password@localhost/testdb
#
## MySQL database URL
#DATABASE_URL_MYSQL=mysql+pymysql://user:password@localhost/testdb
#
## SQLite database URL
#DATABASE_URL_SQLITE=sqlite:///./test.db

