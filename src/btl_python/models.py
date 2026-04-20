"""
SQLAlchemy Models
Định nghĩa các bảng database cho hệ thống quản lý đại lý xe hơi
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, ForeignKey, Index
from sqlalchemy.orm import relationship
from .database.connection import Base


# ============== MODELS ==============

class Car(Base):
    """Thông tin xe"""
    __tablename__ = "cars"
    
    id = Column(Integer, primary_key=True, index=True)
    car_code = Column(String(20), unique=True, nullable=False, index=True)  # XE001
    brand = Column(String(50), nullable=False, index=True)  # Toyota
    model = Column(String(100), nullable=False, index=True)  # Camry 2.5G
    year = Column(Integer, nullable=False, index=True)  # 2023
    color = Column(String(30), index=True)
    price = Column(Float, nullable=False, index=True)  # Giá bán
    stock_quantity = Column(Integer, default=0, index=True)
    status = Column(String(20), default="available", index=True)  # available, sold, reserved
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.now, index=True)
    
    # Relationships
    contracts = relationship("Contract", back_populates="car")
    
    # Indexes for search optimization
    __table_args__ = (
        Index('ix_cars_brand_model', 'brand', 'model'),
        Index('ix_cars_year_status', 'year', 'status'),
        Index('ix_cars_price_stock', 'price', 'stock_quantity'),
    )