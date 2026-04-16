"""
Database Connection Module
Kết nối và quản lý database SQLite với SQLAlchemy
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import StaticPool
import os

# Base class cho models
Base = declarative_base()

# Database URL - SQLite local file
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///data/quanlyxedaily.db"
)

# Create engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
    echo=False  # Set True để debug SQL
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Get database session - dùng cho dependency injection"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Khởi tạo database - tạo tất cả tables"""
    # Import models để Base.metadata nhận diện
    from . import models
    
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized successfully!")


def drop_db():
    """Xóa tất cả tables - cẩn thận khi dùng!"""
    Base.metadata.drop_all(bind=engine)
    print("⚠️  Database dropped!")


if __name__ == "__main__":
    init_db()