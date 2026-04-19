"""
SQLAlchemy Models
Định nghĩa các bảng database cho hệ thống quản lý đại lý xe hơi
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text
from .connection import Base


# ============== MODELS ==============

class Car(Base):
    """Thông tin xe"""
    __tablename__ = "cars"
    
    id = Column(Integer, primary_key=True, index=True)
    car_code = Column(String(20), unique=True, nullable=False)  # XE001
    brand = Column(String(50), nullable=False)  # Toyota
    model = Column(String(100), nullable=False)  # Camry 2.5G
    year = Column(Integer, nullable=False)  # 2023
    color = Column(String(30))
    price = Column(Float, nullable=False)  # Giá bán
    stock_quantity = Column(Integer, default=0)
    status = Column(String(20), default="available")  # available, sold, reserved
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.now)