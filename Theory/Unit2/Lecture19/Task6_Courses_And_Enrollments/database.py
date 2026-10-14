
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Read the database URL or use SQLite by default
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./students.db")

# Create the database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

# Create a factory for database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create the base class for database models
Base = declarative_base()

# Provide a database session to API endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    db = SessionLocal()
    print("Database configuration loaded successfully")
    print("Database URL:", DATABASE_URL)
    db.close()
    print("Database session closed successfully")
