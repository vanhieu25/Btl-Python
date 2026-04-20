"""
Car controller - CRUD operations for car management
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from ..models import Car


class CarController:
    """Controller class for car management operations"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def create_car(self, car_code: str, brand: str, model: str, year: int, 
                   color: str, price: float, stock_quantity: int = 0,
                   description: str = None) -> Car:
        """Create a new car"""
        # Validate required fields
        if not car_code or not brand or not model or year <= 0 or price <= 0:
            raise ValueError("Invalid car data")
        
        # Check if car code already exists
        existing_car = self.db.query(Car).filter(Car.car_code == car_code).first()
        if existing_car:
            raise ValueError(f"Car with code {car_code} already exists")
        
        # Create new car
        new_car = Car(
            car_code=car_code,
            brand=brand,
            model=model,
            year=year,
            color=color,
            price=price,
            stock_quantity=stock_quantity,
            description=description
        )
        
        self.db.add(new_car)
        self.db.commit()
        self.db.refresh(new_car)
        return new_car
    
    def get_car_by_id(self, car_id: int) -> Optional[Car]:
        """Get car by ID"""
        return self.db.query(Car).filter(Car.id == car_id).first()
    
    def get_car_by_code(self, car_code: str) -> Optional[Car]:
        """Get car by code"""
        return self.db.query(Car).filter(Car.car_code == car_code).first()
    
    def get_all_cars(self, skip: int = 0, limit: int = 100) -> List[Car]:
        """Get all cars with pagination"""
        return self.db.query(Car).offset(skip).limit(limit).all()
    
    def update_car(self, car_id: int, **kwargs) -> Optional[Car]:
        """Update car information (except car_code)"""
        car = self.get_car_by_id(car_id)
        if not car:
            return None
        
        # Prevent updating car_code
        if 'car_code' in kwargs:
            del kwargs['car_code']
        
        # Update allowed fields
        allowed_fields = ['brand', 'model', 'year', 'color', 'price', 'stock_quantity', 'description', 'status']
        for field, value in kwargs.items():
            if field in allowed_fields and value is not None:
                setattr(car, field, value)
        
        self.db.commit()
        self.db.refresh(car)
        return car
    
    def delete_car(self, car_id: int) -> bool:
        """Delete car by ID - prevent deletion if car has contracts"""
        car = self.get_car_by_id(car_id)
        if not car:
            return False
        
        # Prevent deletion if car has associated contracts
        if len(car.contracts) > 0:
            raise ValueError(f"Cannot delete car {car.car_code} - it has {len(car.contracts)} associated contract(s)")
        
        self.db.delete(car)
        self.db.commit()
        return True
    
    def search_cars(self, brand: str = None, model: str = None, 
                    year_from: int = None, year_to: int = None,
                    price_from: float = None, price_to: float = None) -> List[Car]:
        """Search cars with filters"""
        query = self.db.query(Car)
        
        if brand:
            query = query.filter(Car.brand.ilike(f"%{brand}%"))
        if model:
            query = query.filter(Car.model.ilike(f"%{model}%"))
        if year_from:
            query = query.filter(Car.year >= year_from)
        if year_to:
            query = query.filter(Car.year <= year_to)
        if price_from:
            query = query.filter(Car.price >= price_from)
        if price_to:
            query = query.filter(Car.price <= price_to)
        
        return query.all()