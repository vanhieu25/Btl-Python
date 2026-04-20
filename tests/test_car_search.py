"""
Unit tests for Car Search & Filter functionality
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


class TestCarSearchFilter:
    """Test suite for Car Search & Filter"""
    
    @classmethod
    def setup_class(cls):
        """Setup test database"""
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
    
    def setup_method(self):
        """Create a new session for each test"""
        self.session = self.Session()
        self.controller = CarController(self.session)
        
        # Create test data
        self.controller.create_car(
            car_code="XE001",
            brand="Toyota",
            model="Camry 2.5G",
            year=2023,
            color="Đen",
            price=1200000000.0,
            stock_quantity=5,
            status="available"
        )
        self.controller.create_car(
            car_code="XE002",
            brand="Honda",
            model="Civic RS",
            year=2024,
            color="Trắng",
            price=850000000.0,
            stock_quantity=0,
            status="sold"
        )
        self.controller.create_car(
            car_code="XE003",
            brand="Toyota",
            model="Corolla Altis",
            year=2023,
            color="Bạc",
            price=750000000.0,
            stock_quantity=2,
            status="available"
        )
        self.controller.create_car(
            car_code="XE004",
            brand="Kia",
            model="Seltos",
            year=2024,
            color="Đỏ",
            price=650000000.0,
            stock_quantity=8,
            status="reserved"
        )
    
    def teardown_method(self):
        """Rollback and close session after each test"""
        self.session.rollback()
        self.session.close()
    
    def test_search_by_brand(self):
        """Test search by brand"""
        cars = self.controller.search_cars(brand="Toyota")
        assert len(cars) == 2
        assert all(car.brand == "Toyota" for car in cars)
    
    def test_search_by_model(self):
        """Test search by model"""
        cars = self.controller.search_cars(model="Civic")
        assert len(cars) == 1
        assert cars[0].model == "Civic RS"
    
    def test_search_by_color(self):
        """Test search by color"""
        cars = self.controller.search_cars(color="Đen")
        assert len(cars) == 1
        assert cars[0].color == "Đen"
    
    def test_search_by_year_range(self):
        """Test search by year range"""
        cars = self.controller.search_cars(year_from=2023, year_to=2023)
        assert len(cars) == 2
        assert all(car.year == 2023 for car in cars)
    
    def test_search_by_price_range(self):
        """Test search by price range"""
        cars = self.controller.search_cars(price_from=700000000.0, price_to=900000000.0)
        assert len(cars) == 2
        assert all(700000000.0 <= car.price <= 900000000.0 for car in cars)
    
    def test_search_by_status(self):
        """Test search by status"""
        cars = self.controller.search_cars(status="available")
        assert len(cars) == 2
        assert all(car.status == "available" for car in cars)
    
    def test_combined_search_criteria(self):
        """Test combined search criteria"""
        cars = self.controller.search_cars(
            brand="Toyota",
            year_from=2023,
            status="available"
        )
        assert len(cars) == 2
        assert all(car.brand == "Toyota" and car.status == "available" for car in cars)
    
    def test_case_insensitive_search(self):
        """Test case-insensitive search"""
        cars_upper = self.controller.search_cars(brand="TOYOTA")
        cars_lower = self.controller.search_cars(brand="toyota")
        cars_mixed = self.controller.search_cars(brand="Toyota")
        
        assert len(cars_upper) == len(cars_lower) == len(cars_mixed) == 2
    
    def test_partial_match_search(self):
        """Test partial match search"""
        cars = self.controller.search_cars(model="Civ")
        assert len(cars) == 1
        assert cars[0].model == "Civic RS"
    
    def test_empty_search_results(self):
        """Test empty search results"""
        cars = self.controller.search_cars(brand="BMW")
        assert len(cars) == 0
    
    def test_search_with_all_criteria(self):
        """Test search with all criteria combined"""
        cars = self.controller.search_cars(
            brand="Toyota",
            model="Camry",
            color="Đen", 
            year_from=2023,
            year_to=2023,
            price_from=1000000000.0,
            price_to=1500000000.0,
            status="available"
        )
        assert len(cars) == 1
        car = cars[0]
        assert car.car_code == "XE001"
        assert car.brand == "Toyota"
        assert car.model == "Camry 2.5G"
        assert car.color == "Đen"
        assert car.year == 2023
        assert car.price == 1200000000.0
        assert car.status == "available"


if __name__ == "__main__":
    pytest.main([__file__])