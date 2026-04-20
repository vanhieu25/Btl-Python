"""
Import/Export service for car management
Handles Excel and CSV file operations for car data
"""

import os
import pandas as pd
from typing import List, Tuple
from sqlalchemy.orm import Session
from ..models import Car
from ..controllers.car_controller import CarController


class ImportExportService:
    """Service class for importing and exporting car data"""
    
    def __init__(self, db: Session):
        self.db = db
        self.controller = CarController(db)
    
    def export_cars_to_excel(self, filename: str, cars: List[Car] = None) -> str:
        """Export cars to Excel file"""
        if cars is None:
            cars = self.controller.get_all_cars()
        
        if not cars:
            raise ValueError("Không có dữ liệu xe để xuất")
        
        # Convert cars to DataFrame
        data = []
        for car in cars:
            data.append({
                'Mã xe': car.car_code,
                'Hãng': car.brand,
                'Dòng xe': car.model,
                'Năm SX': car.year,
                'Màu sắc': car.color or '',
                'Giá bán': car.price,
                'Tồn kho': car.stock_quantity,
                'Trạng thái': car.status,
                'Mô tả': car.description or ''
            })
        
        df = pd.DataFrame(data)
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        # Export to Excel
        df.to_excel(filename, index=False, engine='openpyxl')
        return filename
    
    def export_cars_to_csv(self, filename: str, cars: List[Car] = None) -> str:
        """Export cars to CSV file"""
        if cars is None:
            cars = self.controller.get_all_cars()
        
        if not cars:
            raise ValueError("Không có dữ liệu xe để xuất")
        
        # Convert cars to DataFrame
        data = []
        for car in cars:
            data.append({
                'Mã xe': car.car_code,
                'Hãng': car.brand,
                'Dòng xe': car.model,
                'Năm SX': car.year,
                'Màu sắc': car.color or '',
                'Giá bán': car.price,
                'Tồn kho': car.stock_quantity,
                'Trạng thái': car.status,
                'Mô tả': car.description or ''
            })
        
        df = pd.DataFrame(data)
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        # Export to CSV
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        return filename
    
    def import_cars_from_excel(self, filename: str, skip_duplicates: bool = True) -> Tuple[int, int, List[str]]:
        """Import cars from Excel file
        Returns: (success_count, error_count, error_messages)
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Không tìm thấy file: {filename}")
        
        try:
            # Read Excel file
            df = pd.read_excel(filename, engine='openpyxl')
            return self._process_import_dataframe(df, skip_duplicates)
        except Exception as e:
            raise ValueError(f"Lỗi khi đọc file Excel: {str(e)}")
    
    def import_cars_from_csv(self, filename: str, skip_duplicates: bool = True) -> Tuple[int, int, List[str]]:
        """Import cars from CSV file
        Returns: (success_count, error_count, error_messages)
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Không tìm thấy file: {filename}")
        
        try:
            # Read CSV file
            df = pd.read_csv(filename, encoding='utf-8-sig')
            return self._process_import_dataframe(df, skip_duplicates)
        except Exception as e:
            raise ValueError(f"Lỗi khi đọc file CSV: {str(e)}")
    
    def _process_import_dataframe(self, df: pd.DataFrame, skip_duplicates: bool = True) -> Tuple[int, int, List[str]]:
        """Process DataFrame for import"""
        success_count = 0
        error_count = 0
        error_messages = []
        
        # Required columns
        required_columns = ['Mã xe', 'Hãng', 'Dòng xe', 'Năm SX', 'Giá bán']
        
        # Check if all required columns exist
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Thiếu các cột bắt buộc: {', '.join(missing_columns)}")
        
        # Process each row
        for index, row in df.iterrows():
            try:
                # Extract data with defaults
                car_code = str(row['Mã xe']).strip() if pd.notna(row['Mã xe']) else None
                brand = str(row['Hãng']).strip() if pd.notna(row['Hãng']) else None
                model = str(row['Dòng xe']).strip() if pd.notna(row['Dòng xe']) else None
                year = int(row['Năm SX']) if pd.notna(row['Năm SX']) else None
                color = str(row['Màu sắc']).strip() if pd.notna(row['Màu sắc']) else None
                price = float(row['Giá bán']) if pd.notna(row['Giá bán']) else None
                stock_quantity = int(row['Tồn kho']) if pd.notna(row['Tồn kho']) else 0
                status = str(row['Trạng thái']).strip() if pd.notna(row['Trạng thái']) else 'available'
                description = str(row['Mô tả']).strip() if pd.notna(row['Mô tả']) else None
                
                # Validate required fields
                if not car_code or not brand or not model or not year or not price:
                    error_msg = f"Dòng {index + 2}: Thiếu thông tin bắt buộc"
                    error_messages.append(error_msg)
                    error_count += 1
                    continue
                
                # Validate data types
                if year <= 0 or price <= 0 or stock_quantity < 0:
                    error_msg = f"Dòng {index + 2}: Dữ liệu không hợp lệ (năm, giá, tồn kho)"
                    error_messages.append(error_msg)
                    error_count += 1
                    continue
                
                # Check if car already exists
                existing_car = self.controller.get_car_by_code(car_code)
                if existing_car:
                    if skip_duplicates:
                        # Skip duplicate
                        continue
                    else:
                        # Update existing car
                        self.controller.update_car(
                            existing_car.id,
                            brand=brand,
                            model=model,
                            year=year,
                            color=color,
                            price=price,
                            stock_quantity=stock_quantity,
                            status=status,
                            description=description
                        )
                else:
                    # Create new car
                    self.controller.create_car(
                        car_code=car_code,
                        brand=brand,
                        model=model,
                        year=year,
                        color=color,
                        price=price,
                        stock_quantity=stock_quantity,
                        status=status,
                        description=description
                    )
                
                success_count += 1
                
            except Exception as e:
                error_msg = f"Dòng {index + 2}: {str(e)}"
                error_messages.append(error_msg)
                error_count += 1
        
        return success_count, error_count, error_messages