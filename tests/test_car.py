"""
Unit tests for Car Management functionality
"""

import os
import sys
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from btl_python.models import Car, Base
from btl_python.controllers.car_controller import CarController
from btl_python.database.connection import Base as ConnectionBase


class TestCarManagement:
    """Test suite for Car Management"""
    
    @classmethod
    def setup_class(cls):
        """Setup test database"""
        # Create in-memory SQLite database for testing
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
    
    def setup_method(self):
        """Create a new session for each test"""
        self.session = self.Session()
        self.controller = CarController(self.session)
    
    def teardown_method(self):
        """Rollback and close session after each test"""
        self.session.rollback()
        self.session.close()
    
    def test_create_car_success(self):
        """Test successful car creation"""
        car = self.controller.create_car(
            car_code="XE001",
            brand="Toyota",
            model="Camry 2.5G",
            year=2023,
            color="Đen",
            price=1200000000.0,
            stock_quantity=5
        )
        
        assert car is not None
        assert car.car_code == "XE001"
        assert car.brand == "Toyota"
        assert car.model == "Camry 2.5G"
        assert car.year == 2023
        assert car.price == 1200000000.0
        assert car.stock_quantity == 5
    
    def test_create_car_duplicate_code(self):
        """Test creating car with duplicate code"""
        # Create first car
        self.controller.create_car(
            car_code="XE001",
            brand="Toyota",
            model="Camry 2.5G",
            year=2023,
            color="Đen",
            price=1200000000.0
        )
        
        # Try to create second car with same code
        with pytest.raises(ValueError, match="already exists"):
            self.controller.create_car(
                car_code="XE001",
                brand="Honda",
                model="Civic",
                year=2024,
                color="Trắng",
                price=850000000.0
            )
    
    def test_create_car_invalid_data(self):
        """Test creating car with invalid data"""
        # Test negative price
        with pytest.raises(ValueError):
            self.controller.create_car(
                car_code="XE002",
                brand="Toyota",
                model="Camry",
                year=2023,
                color="Đen",
                price=-1000000.0
            )
        
        # Test invalid year
        with pytest.raises(ValueError):
            self.controller.create_car(
                car_code="XE002",
                brand="Toyota",
                model="Camry",
                year=0,
                color="Đen",
                price=1200000000.0
            )
    
    def test_get_all_cars(self):
        """Test getting all cars"""
        # Create test cars
        self.controller.create_car(
            car_code="XE001",
            brand="Toyota",
            model="Camry",
            year=2023,
            price=1200000000.0
        )
        self.controller.create_car(
            car_code="XE002",
            brand="Honda",
            model="Civic",
            year=2024,
            price=850000000.0
        )
        
        cars = self.controller.get_all_cars()
        assert len(cars) == 2
        
        # Check order
        assert cars[0].car_code == "XE001"
        assert cars[1].car_code == "XE002"
    
    def test_update_car(self):
        """Test updating car information"""
        # Create car
        car = self.controller.create_car(
            car_code="XE001",
            brand="Toyota",
            model="Camry",
            year=2023,
            price=1200000000.0,
            stock_quantity=5
        )
        
        # Update car (should not update car_code)
        updated_car = self.controller.update_car(
            car.id,
            brand="Toyota Updated",
            model="Camry Updated",
            year=2024,
            price=1300000000.0,
            stock_quantity=10,
            car_code="XE999"  # This should be ignored
        )
        
        assert updated_car is not None
        assert updated_car.brand == "Toyota Updated"
        assert updated_car.model == "Camry Updated"
        assert updated_car.year == 2024
        assert updated_car.price == 1300000000.0
        assert updated_car.stock_quantity == 10
        assert updated_car.car_code == "XE001"  # Should not change
    
    def test_delete_car(self):
        """Test deleting car"""
        # Create car
        car = self.controller.create_car(
            car_code="XE001",
            brand="Toyota",
            model="Camry",
            year=2023,
            price=1200000000.0
        )
        
        # Delete car
        result = self.controller.delete_car(car.id)
        assert result is True
        
        # Verify car is deleted
        deleted_car = self.controller.get_car_by_id(car.id)
        assert deleted_car is None
    
    def test_search_cars(self):
        """Test searching cars"""
        # Create test cars
        self.controller.create_car(
            car_code="XE001",
            brand="Toyota",
            model="Camry",
            year=2023,
            price=1200000000.0
        )
        self.controller.create_car(
            car_code="XE002",
            brand="Honda",
            model="Civic",
            year=2024,
            price=850000000.0
        )
        self.controller.create_car(
            car_code="XE003",
            brand="Toyota",
            model="Corolla",
            year=2023,
            price=750000000.0
        )
        
        # Search by brand
        toyota_cars = self.controller.search_cars(brand="Toyota")
        assert len(toyota_cars) == 2
        
        # Search by year range
        cars_2023 = self.controller.search_cars(year_from=2023, year_to=2023)
        assert len(cars_2023) == 2
        
        # Search by price range
        expensive_cars = self.controller.search_cars(price_from=1000000000.0)
        assert len(expensive_cars) == 1
        assert expensive_cars[0].car_code == "XE001"


if __name__ == "__main__":
    pytest.main([__file__])