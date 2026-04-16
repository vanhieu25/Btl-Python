"""
Initialize Database Script
Tạo database + sample data cho testing
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import init_db, drop_db, engine
from database.models import (
    User, Car, Customer, Contract, Warranty, Promotion,
    Accessory, Supplier, Complaint, Inventory, Base
)
from sqlalchemy.orm import Session
import bcrypt
from datetime import datetime, timedelta


def create_sample_users(db: Session):
    """Tạo sample users"""
    users = [
        {
            "username": "admin",
            "password": "admin123",
            "full_name": "Quản Trị Viên",
            "email": "admin@dealer.com",
            "role": "admin"
        },
        {
            "username": "sales01",
            "password": "sales123",
            "full_name": "Nguyễn Văn Bán",
            "email": "sales01@dealer.com",
            "role": "sales"
        },
        {
            "username": "manager01",
            "password": "manager123",
            "full_name": "Trần Thị Quản",
            "email": "manager@dealer.com",
            "role": "manager"
        }
    ]
    
    for user_data in users:
        password_hash = bcrypt.hashpw(
            user_data["password"].encode(),
            bcrypt.gensalt()
        ).decode()
        
        user = User(
            username=user_data["username"],
            password_hash=password_hash,
            full_name=user_data["full_name"],
            email=user_data["email"],
            role=user_data["role"]
        )
        db.add(user)
    
    db.commit()
    print("✅ Created 3 sample users")


def create_sample_cars(db: Session):
    """Tạo sample cars"""
    cars = [
        Car(car_code="XE001", brand="Toyota", model="Camry 2.5G", year=2023, 
            color="Đen", price=1200000000, import_price=1100000000, stock_quantity=5),
        Car(car_code="XE002", brand="Honda", model="Civic RS", year=2024,
            color="Trắng", price=850000000, import_price=780000000, stock_quantity=3),
        Car(car_code="XE003", brand="Hyundai", model="Santa Fe", year=2023,
            color="Xám", price=1100000000, import_price=1000000000, stock_quantity=0),
        Car(car_code="XE004", brand="Kia", model="Seltos", year=2024,
            color="Đỏ", price=650000000, import_price=600000000, stock_quantity=8),
        Car(car_code="XE005", brand="Mazda", model="CX-5", year=2023,
            color="Xanh", price=900000000, import_price=820000000, stock_quantity=2),
    ]
    
    db.add_all(cars)
    db.commit()
    print("✅ Created 5 sample cars")


def create_sample_customers(db: Session):
    """Tạo sample customers"""
    customers = [
        Customer(customer_code="KH001", full_name="Nguyễn Văn An", 
                customer_type="individual", phone="0901234567",
                email="an.nguyen@email.com", address="123 Nguyễn Văn A, Q.1, TP.HCM"),
        Customer(customer_code="KH002", full_name="Công ty TNHH B",
                customer_type="company", phone="0912345678",
                email="contact@congtyb.com", address="456 Lê Lợi, Q.3, TP.HCM",
                tax_code="0123456789"),
    ]
    
    db.add_all(customers)
    db.commit()
    print("✅ Created 2 sample customers")


def create_sample_promotions(db: Session):
    """Tạo sample promotions"""
    promotions = [
        Promotion(
            name="Giảm giá mùa hè 2024",
            description="Giảm 50 triệu cho tất cả xe Toyota",
            discount_type="fixed",
            discount_value=50000000,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=30),
            applicable_brands="Toyota"
        ),
    ]
    
    db.add_all(promotions)
    db.commit()
    print("✅ Created 1 sample promotion")


def create_sample_suppliers(db: Session):
    """Tạo sample suppliers"""
    suppliers = [
        Supplier(name="Toyota Việt Nam", contact_person="Mr. Toyota",
                phone="0281234567", email="sales@toyota.vn",
                address="Số 1 Đường Toyota, Q.7, TP.HCM", rating=5.0),
        Supplier(name="Honda Việt Nam", contact_person="Ms. Honda",
                phone="0287654321", email="sales@honda.vn",
                address="Số 2 Đường Honda, Q.7, TP.HCM", rating=4.8),
    ]
    
    db.add_all(suppliers)
    db.commit()
    print("✅ Created 2 sample suppliers")


def init_sample_data():
    """Khởi tạo database với sample data"""
    from database.connection import SessionLocal
    
    print("🚀 Initializing database with sample data...\n")
    
    # Tạo tables
    init_db()
    
    # Tạo sample data
    db = SessionLocal()
    try:
        create_sample_users(db)
        create_sample_cars(db)
        create_sample_customers(db)
        create_sample_promotions(db)
        create_sample_suppliers(db)
        
        print("\n✅ Database initialized with sample data successfully!")
        print("\n📋 Sample accounts:")
        print("  - admin / admin123")
        print("  - sales01 / sales123")
        print("  - manager01 / manager123")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--reset":
        print("⚠️  Resetting database...")
        drop_db()
    
    init_sample_data()