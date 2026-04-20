"""
Unit tests for Car Import/Export functionality
"""

import os
import sys
import pytest
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from btl_python.models import Car, Base
from btl_python.services.import_export_service import ImportExportService


class TestCarImportExport:
    """Test suite for Car Import/Export"""
    
    @classmethod
    def setup_class(cls):
        """Setup test database"""
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        
        # Create test directory
        cls.test_dir = "test_files"
        os.makedirs(cls.test_dir, exist_ok=True)
    
    def setup_method(self):
        """Create a new session for each test"""
        self.session = self.Session()
        self.service = ImportExportService(self.session)
    
    def teardown_method(self):
        """Rollback and close session after each test"""
        self.session.rollback()
        self.session.close()
    
    @classmethod
    def teardown_class(cls):
        """Clean up test files"""
        if os.path.exists(cls.test_dir):
            for file in os.listdir(cls.test_dir):
                os.remove(os.path.join(cls.test_dir, file))
            os.rmdir(cls.test_dir)
    
    def test_export_to_excel(self):
        """Test export cars to Excel"""
        # Create test car
        from btl_python.controllers.car_controller import CarController
        controller = CarController(self.session)
        controller.create_car(
            car_code="XE001",
            brand="Toyota",
            model="Camry",
            year=2023,
            price=1200000000.0
        )
        
        # Export to Excel
        filename = os.path.join(self.test_dir, "test_export.xlsx")
        result = self.service.export_cars_to_excel(filename)
        
        assert os.path.exists(result)
        
        # Verify content
        df = pd.read_excel(result, engine='openpyxl')
        assert len(df) == 1
        assert df.iloc[0]['Mã xe'] == "XE001"
        assert df.iloc[0]['Hãng'] == "Toyota"
    
    def test_export_to_csv(self):
        """Test export cars to CSV"""
        # Create test car
        from btl_python.controllers.car_controller import CarController
        controller = CarController(self.session)
        controller.create_car(
            car_code="XE001",
            brand="Toyota",
            model="Camry",
            year=2023,
            price=1200000000.0
        )
        
        # Export to CSV
        filename = os.path.join(self.test_dir, "test_export.csv")
        result = self.service.export_cars_to_csv(filename)
        
        assert os.path.exists(result)
        
        # Verify content
        df = pd.read_csv(result, encoding='utf-8-sig')
        assert len(df) == 1
        assert df.iloc[0]['Mã xe'] == "XE001"
        assert df.iloc[0]['Hãng'] == "Toyota"
    
    def test_import_from_excel(self):
        """Test import cars from Excel"""
        # Create test Excel file
        test_data = {
            'Mã xe': ['XE002', 'XE003'],
            'Hãng': ['Honda', 'Kia'],
            'Dòng xe': ['Civic', 'Seltos'],
            'Năm SX': [2024, 2023],
            'Giá bán': [850000000.0, 650000000.0],
            'Tồn kho': [5, 3],
            'Trạng thái': ['available', 'reserved'],
            'Mô tả': ['', 'Xe mới']
        }
        df = pd.DataFrame(test_data)
        filename = os.path.join(self.test_dir, "test_import.xlsx")
        df.to_excel(filename, index=False, engine='openpyxl')
        
        # Import from Excel
        success_count, error_count, errors = self.service.import_cars_from_excel(filename)
        
        assert success_count == 2
        assert error_count == 0
        assert len(errors) == 0
        
        # Verify imported data
        cars = self.service.controller.get_all_cars()
        assert len(cars) == 2
        assert cars[0].car_code == "XE002"
        assert cars[1].car_code == "XE003"
    
    def test_import_from_csv(self):
        """Test import cars from CSV"""
        # Create test CSV file
        test_data = {
            'Mã xe': ['XE004', 'XE005'],
            'Hãng': ['Mazda', 'Hyundai'],
            'Dòng xe': ['CX-5', 'Tucson'],
            'Năm SX': [2023, 2024],
            'Giá bán': [950000000.0, 750000000.0],
            'Tồn kho': [2, 7],
            'Trạng thái': ['available', 'available'],
            'Mô tả': ['', '']
        }
        df = pd.DataFrame(test_data)
        filename = os.path.join(self.test_dir, "test_import.csv")
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        
        # Import from CSV
        success_count, error_count, errors = self.service.import_cars_from_csv(filename)
        
        assert success_count == 2
        assert error_count == 0
        assert len(errors) == 0
        
        # Verify imported data
        cars = self.service.controller.get_all_cars()
        assert len(cars) == 2
        assert cars[0].car_code == "XE004"
        assert cars[1].car_code == "XE005"
    
    def test_import_with_duplicates(self):
        """Test import with duplicate handling"""
        # Create initial car
        from btl_python.controllers.car_controller import CarController
        controller = CarController(self.session)
        controller.create_car(
            car_code="XE001",
            brand="Toyota",
            model="Camry",
            year=2023,
            price=1200000000.0
        )
        
        # Create test Excel file with duplicate
        test_data = {
            'Mã xe': ['XE001', 'XE002'],  # XE001 is duplicate
            'Hãng': ['Toyota Updated', 'Honda'],
            'Dòng xe': ['Camry Updated', 'Civic'],
            'Năm SX': [2024, 2024],
            'Giá bán': [1300000000.0, 850000000.0],
            'Tồn kho': [10, 5],
            'Trạng thái': ['available', 'available'],
            'Mô tả': ['', '']
        }
        df = pd.DataFrame(test_data)
        filename = os.path.join(self.test_dir, "test_duplicate.xlsx")
        df.to_excel(filename, index=False, engine='openpyxl')
        
        # Import with skip duplicates
        success_count, error_count, errors = self.service.import_cars_from_excel(
            filename, skip_duplicates=True
        )
        
        assert success_count == 1  # Only XE002 should be imported
        assert error_count == 0
        
        # Verify original car unchanged (skip_duplicates=True)
        original_car = controller.get_car_by_code("XE001")
        assert original_car.model == "Camry"  # Should not be updated
        
        # Verify new car imported
        new_car = controller.get_car_by_code("XE002")
        assert new_car is not None
    
    def test_import_missing_required_columns(self):
        """Test import with missing required columns"""
        # Create test Excel file without required columns
        test_data = {
            'Mã xe': ['XE001'],
            'Hãng': ['Toyota'],
            # Missing 'Dòng xe' and 'Giá bán'
            'Năm SX': [2023]
        }
        df = pd.DataFrame(test_data)
        filename = os.path.join(self.test_dir, "test_missing_cols.xlsx")
        df.to_excel(filename, index=False, engine='openpyxl')
        
        # Import should fail
        with pytest.raises(ValueError, match="Thiếu các cột bắt buộc"):
            self.service.import_cars_from_excel(filename)
    
    def test_import_invalid_data(self):
        """Test import with invalid data"""
        # Create test Excel file with invalid data
        test_data = {
            'Mã xe': ['XE001', 'XE002'],
            'Hãng': ['Toyota', 'Honda'],
            'Dòng xe': ['Camry', 'Civic'],
            'Năm SX': [-1, 2024],  # Invalid year
            'Giá bán': [1200000000.0, -500000.0],  # Invalid price
            'Tồn kho': [5, -2],  # Invalid stock
            'Trạng thái': ['available', 'available'],
            'Mô tả': ['', '']
        }
        df = pd.DataFrame(test_data)
        filename = os.path.join(self.test_dir, "test_invalid_data.xlsx")
        df.to_excel(filename, index=False, engine='openpyxl')
        
        # Import should process valid rows and report errors
        success_count, error_count, errors = self.service.import_cars_from_excel(filename)
        
        assert success_count == 0  # Both rows have invalid data
        assert error_count == 2
        assert len(errors) == 2


if __name__ == "__main__":
    pytest.main([__file__])