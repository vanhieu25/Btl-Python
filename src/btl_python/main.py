"""
Main entry point for Btl Python
"""

from .database.connection import engine, SessionLocal
from .models import Base

def init_database():
    """Initialize database tables"""
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_database()
    print("Btl Python initialized successfully!")