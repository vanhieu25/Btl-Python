"""
SQLAlchemy Models
Định nghĩa các bảng database cho hệ thống quản lý đại lý xe hơi
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database.connection import Base
import enum


# Enums
class UserRole(enum.Enum):
    ADMIN = "admin"
    SALES = "sales"
    MANAGER = "manager"
    ACCOUNTANT = "accountant"


class ContractStatus(enum.Enum):
    NEW = "new"
    PAID = "paid"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class CustomerType(enum.Enum):
    INDIVIDUAL = "individual"
    COMPANY = "company"


class WarrantyStatus(enum.Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    CLAIMED = "claimed"


class ComplaintStatus(enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    RESOLVED = "resolved"
    CLOSED = "closed"


# ============== MODELS ==============

class User(Base):
    """Nhân viên / Admin hệ thống"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)  # bcrypt hash
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    role = Column(Enum(UserRole), default=UserRole.SALES)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    
    # Relationships
    contracts_created = relationship("Contract", back_populates="created_by")
    complaints_handled = relationship("Complaint", back_populates="handled_by")


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
    import_price = Column(Float)  # Giá nhập
    stock_quantity = Column(Integer, default=0)
    status = Column(String(20), default="available")  # available, sold, reserved
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    
    # Relationships
    contracts = relationship("Contract", back_populates="car")
    inventory_logs = relationship("Inventory", back_populates="car")


class Customer(Base):
    """Khách hàng"""
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True, index=True)
    customer_code = Column(String(20), unique=True, nullable=False)  # KH001
    full_name = Column(String(100), nullable=False)
    customer_type = Column(Enum(CustomerType), default=CustomerType.INDIVIDUAL)
    phone = Column(String(20), nullable=False)
    email = Column(String(100))
    address = Column(Text)
    tax_code = Column(String(50))  # Mã số thuế (nếu doanh nghiệp)
    is_vip = Column(Boolean, default=False)
    total_contracts = Column(Integer, default=0)
    total_value = Column(Float, default=0)  # Tổng giá trị mua hàng
    created_at = Column(DateTime, default=datetime.now)
    
    # Relationships
    contracts = relationship("Contract", back_populates="customer")
    warranties = relationship("Warranty", back_populates="customer")


class Contract(Base):
    """Hợp đồng bán xe"""
    __tablename__ = "contracts"
    
    id = Column(Integer, primary_key=True, index=True)
    contract_code = Column(String(20), unique=True, nullable=False)  # HD0001
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    car_id = Column(Integer, ForeignKey("cars.id"), nullable=False)
    created_by_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Giá
    car_price = Column(Float, nullable=False)
    accessories_price = Column(Float, default=0)
    discount = Column(Float, default=0)
    total_price = Column(Float, nullable=False)
    deposit = Column(Float, default=0)
    paid_amount = Column(Float, default=0)
    
    # Thông tin
    status = Column(Enum(ContractStatus), default=ContractStatus.NEW)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    delivered_at = Column(DateTime)
    
    # Relationships
    customer = relationship("Customer", back_populates="contracts")
    car = relationship("Car", back_populates="contracts")
    created_by = relationship("User", back_populates="contracts_created")
    warranty = relationship("Warranty", back_populates="contract", uselist=False)


class Warranty(Base):
    """Bảo hành xe"""
    __tablename__ = "warranties"
    
    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, ForeignKey("contracts.id"), unique=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    
    warranty_months = Column(Integer, default=36)  # Tháng bảo hành
    start_date = Column(DateTime, default=datetime.now)
    end_date = Column(DateTime)
    status = Column(Enum(WarrantyStatus), default=WarrantyStatus.ACTIVE)
    
    # Relationships
    contract = relationship("Contract", back_populates="warranty")
    customer = relationship("Customer", back_populates="warranties")
    claims = relationship("WarrantyClaim", back_populates="warranty")


class WarrantyClaim(Base):
    """Yêu cầu bảo hành"""
    __tablename__ = "warranty_claims"
    
    id = Column(Integer, primary_key=True, index=True)
    warranty_id = Column(Integer, ForeignKey("warranties.id"), nullable=False)
    claim_date = Column(DateTime, default=datetime.now)
    description = Column(Text, nullable=False)
    repair_cost = Column(Float, default=0)
    is_free = Column(Boolean, default=True)  # Có miễn phí không
    
    # Relationships
    warranty = relationship("Warranty", back_populates="claims")


class Promotion(Base):
    """Chương trình khuyến mãi"""
    __tablename__ = "promotions"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    discount_type = Column(String(20))  # fixed, percentage
    discount_value = Column(Float)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    is_active = Column(Boolean, default=True)
    applicable_brands = Column(String(255))  # Toyota,Honda (comma separated)
    created_at = Column(DateTime, default=datetime.now)


class Accessory(Base):
    """Phụ kiện xe"""
    __tablename__ = "accessories"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(200), nullable=False)
    category = Column(String(50))  # interior, exterior, electronics
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)
    description = Column(Text)


class Supplier(Base):
    """Nhà cung cấp"""
    __tablename__ = "suppliers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    contact_person = Column(String(100))
    phone = Column(String(20))
    email = Column(String(100))
    address = Column(Text)
    rating = Column(Float, default=5.0)  # 1-5
    created_at = Column(DateTime, default=datetime.now)
    
    # Relationships
    purchases = relationship("PurchaseOrder", back_populates="supplier")


class PurchaseOrder(Base):
    """Đơn đặt hàng từ NCC"""
    __tablename__ = "purchase_orders"
    
    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    order_date = Column(DateTime, default=datetime.now)
    total_amount = Column(Float, default=0)
    status = Column(String(20), default="pending")  # pending, received, cancelled
    notes = Column(Text)
    
    # Relationships
    supplier = relationship("Supplier", back_populates="purchases")


class Complaint(Base):
    """Khiếu nại khách hàng"""
    __tablename__ = "complaints"
    
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    handled_by_id = Column(Integer, ForeignKey("users.id"))
    
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    priority = Column(String(20), default="medium")  # low, medium, high
    status = Column(Enum(ComplaintStatus), default=ComplaintStatus.PENDING)
    resolution = Column(Text)
    satisfaction_score = Column(Integer)  # 1-5
    created_at = Column(DateTime, default=datetime.now)
    resolved_at = Column(DateTime)
    
    # Relationships
    handled_by = relationship("User", back_populates="complaints_handled")


class Inventory(Base):
    """Lịch sử tồn kho / nhập xuất"""
    __tablename__ = "inventory"
    
    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("cars.id"), nullable=False)
    change_type = Column(String(20), nullable=False)  # import, export, sale
    quantity_change = Column(Integer, nullable=False)  # +1, -1
    previous_stock = Column(Integer)
    new_stock = Column(Integer)
    reference_id = Column(String(50))  # Mã HĐ hoặc mã nhập
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    
    # Relationships
    car = relationship("Car", back_populates="inventory_logs")